import os
import re
import csv
import requests
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# Configuration
GITHUB_REPO = "https://api.github.com/repos/hashicorp/terraform-provider-azurerm"
DOCS_PATH = "website/docs/r"  # Relative path in the repo
OUTPUT_FILE = "terraform_resources_with_tags.csv"
CSV_URL = "https://raw.githubusercontent.com/tfitzmac/resource-capabilities/main/tag-support.csv"

def fetch_github_files():
    """Fetch all markdown files from GitHub repo without cloning"""
    url = f"{GITHUB_REPO}/contents/{DOCS_PATH}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"  # Optional for higher rate limits
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        files = []
        for item in response.json():
            if item['name'].endswith('.markdown'):
                files.append({
                    'name': item['name'],
                    'download_url': item['download_url']
                })
        return files
    except Exception as e:
        print(f"Error fetching files from GitHub: {e}")
        raise

def get_markdown_content(file_info):
    """Download content of a single markdown file"""
    try:
        response = requests.get(file_info['download_url'])
        response.raise_for_status()
        return {
            'name': file_info['name'],
            'content': response.text
        }
    except Exception as e:
        print(f"Error downloading {file_info['name']}: {e}")
        return None

def find_resource_matches(resource, markdown_contents):
    """Find matches in in-memory markdown contents"""
    segments = resource.split('/')
    search_pattern = re.escape(segments[0].lower())
    for segment in segments[1:]:
        if not segment or ' ' in segment:
            return None
        search_pattern += r'/[^/]+'
    
    matches = []
    for file_content in markdown_contents:
        if file_content is None:
            continue
        try:
            for match in re.finditer(
                r'terraform\s+import\s+(azurerm_\w+)[^\n]*/providers/([^\s/]+(?:/[^/\s]+)*)',
                file_content['content'],
                re.IGNORECASE
            ):
                tf_resource = match.group(1)
                provider_path = match.group(2).lower()
                if re.fullmatch(search_pattern, provider_path):
                    azure_type = '/'.join(provider_path.split('/')[1:])
                    matches.append((tf_resource, segments[0], azure_type))
        except Exception as e:
            print(f"Error processing {file_content.get('name', 'unknown')}: {e}")
    return matches if matches else None

def main():
    try:
        # 1. Fetch supported resources from CSV
        resources = fetch_supported_resources()
        
        # 2. Get markdown files from GitHub
        print("Fetching markdown files from GitHub...")
        markdown_files = fetch_github_files()
        print(f"Found {len(markdown_files)} markdown files")
        
        # 3. Download all markdown contents in parallel
        with ThreadPoolExecutor(max_workers=8) as executor:
            markdown_contents = list(filter(None, executor.map(get_markdown_content, markdown_files)))
        
        # 4. Process resources against markdown contents
        print("Searching for matching resources...")
        with ThreadPoolExecutor(max_workers=8) as executor:
            find_matches = partial(find_resource_matches, markdown_contents=markdown_contents)
            results = list(filter(None, executor.map(find_matches, resources)))
        
        # 5. Process and save results
        flat_results = [item for sublist in results for item in sublist]
        unique_results = sorted(set(flat_results), key=lambda x: x[0])
        
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["terraform_resource", "provider_name", "azure_resource_type"])
            writer.writerows(unique_results)
            
        print(f"\n✅ Found {len(unique_results)} matches. Results saved to {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise

if __name__ == "__main__":
    main()
