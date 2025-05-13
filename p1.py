import os
import re
import csv
import requests
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# Configuration
GITHUB_REPO = "https://api.github.com/repos/hashicorp/terraform-provider-azurerm"
DOCS_PATH = "website/docs/r"
OUTPUT_FILE = "terraform_resources_with_tags.csv"
CSV_URL = "https://raw.githubusercontent.com/tfitzmac/resource-capabilities/main/tag-support.csv"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')

def fetch_supported_resources():
    """Fetch resources that support tags from CSV"""
    try:
        response = requests.get(CSV_URL, timeout=30)
        response.raise_for_status()
        reader = csv.DictReader(response.text.splitlines())
        return [
            f"{row['providerName'].replace(' ', '.').lower()}/{row['resourceType']}"
            for row in reader if row.get('supportsTags', '').strip().upper() == 'TRUE'
        ]
    except Exception as e:
        print(f"Error fetching CSV: {e}")
        raise

def fetch_all_github_files():
    """Fetch ALL markdown files with pagination support"""
    url = f"{GITHUB_REPO}/contents/{DOCS_PATH}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    all_files = []
    page = 1
    while True:
        try:
            response = requests.get(f"{url}?page={page}", headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not data:
                break
            all_files.extend([
                item for item in data 
                if isinstance(item, dict) and item['name'].endswith('.markdown')
            ])
            page += 1
            # Check rate limits
            if 'X-RateLimit-Remaining' in response.headers:
                if int(response.headers['X-RateLimit-Remaining']) < 10:
                    print("Warning: Approaching GitHub rate limit")
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
    return all_files

def get_file_content(file_info):
    """Get content with retry logic"""
    for attempt in range(3):
        try:
            response = requests.get(file_info['download_url'], timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            if attempt == 2:
                print(f"Failed to download {file_info['name']}: {e}")
                return None
            time.sleep(2 ** attempt)

def main():
    try:
        print("Fetching supported resources...")
        resources = fetch_supported_resources()
        print(f"Found {len(resources)} taggable resources")
        
        print("Fetching markdown files from GitHub...")
        files = fetch_all_github_files()
        print(f"Found {len(files)} markdown files")
        
        print("Downloading contents...")
        with ThreadPoolExecutor(max_workers=10) as executor:
            contents = list(filter(None, executor.map(
                lambda f: {'name': f['name'], 'content': get_file_content(f)},
                files
            )))
        
        print("Processing matches...")
        with ThreadPoolExecutor(max_workers=8) as executor:
            find_matches = partial(find_resource_matches, markdown_contents=contents)
            results = list(filter(None, executor.map(find_matches, resources)))
        
        # Process results
        flat_results = [item for sublist in results for item in sublist]
        unique_results = sorted(set(flat_results), key=lambda x: x[0])
        
        print(f"\nFound {len(unique_results)} unique matches")
        print(f"Saving to {OUTPUT_FILE}")
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["terraform_resource", "provider_name", "azure_resource_type"])
            writer.writerows(unique_results)
            
        print("Done!")
        
    except Exception as e:
        print(f"\nError: {e}")
        raise

if __name__ == "__main__":
    import time
    main()
# import os
# import re
# import csv
# import requests
# from concurrent.futures import ThreadPoolExecutor
# from functools import partial

# # Configuration
# GITHUB_REPO = "https://api.github.com/repos/hashicorp/terraform-provider-azurerm"
# DOCS_PATH = "website/docs/r"
# OUTPUT_FILE = "terraform_resources_with_tags.csv"
# CSV_URL = "https://raw.githubusercontent.com/tfitzmac/resource-capabilities/main/tag-support.csv"

# def fetch_supported_resources():
#     """Fetch resources that support tags from CSV"""
#     try:
#         response = requests.get(CSV_URL, timeout=10)
#         response.raise_for_status()
#         reader = csv.DictReader(response.text.splitlines())
        
#         supported_resources = []
#         for row in reader:
#             if row.get('supportsTags', '').strip().upper() == 'TRUE':
#                 provider = row['providerName'].replace(" ", ".").lower()
#                 resource_type = row['resourceType']
#                 supported_resources.append(f"{provider}/{resource_type}")
        
#         print(f"Found {len(supported_resources)} resources supporting tags")
#         return supported_resources
    
#     except Exception as e:
#         print(f"Error fetching CSV: {e}")
#         raise

# def fetch_github_files():
#     """Fetch all markdown files from GitHub repo without cloning"""
#     url = f"{GITHUB_REPO}/contents/{DOCS_PATH}"
#     headers = {
#         "Accept": "application/vnd.github.v3+json",
#         "Authorization": f"token {os.getenv('GITHUB_TOKEN')}" if os.getenv('GITHUB_TOKEN') else None
#     }
    
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         files = []
#         for item in response.json():
#             if item['name'].endswith('.markdown'):
#                 files.append({
#                     'name': item['name'],
#                     'download_url': item['download_url']
#                 })
#         return files
#     except Exception as e:
#         print(f"Error fetching files from GitHub: {e}")
#         raise

# def get_markdown_content(file_info):
#     """Download content of a single markdown file"""
#     try:
#         response = requests.get(file_info['download_url'])
#         response.raise_for_status()
#         return {
#             'name': file_info['name'],
#             'content': response.text
#         }
#     except Exception as e:
#         print(f"Error downloading {file_info['name']}: {e}")
#         return None

# def find_resource_matches(resource, markdown_contents):
#     """Find matches in in-memory markdown contents"""
#     segments = resource.split('/')
#     search_pattern = re.escape(segments[0].lower())
#     for segment in segments[1:]:
#         if not segment or ' ' in segment:
#             return None
#         search_pattern += r'/[^/]+'
    
#     matches = []
#     for file_content in markdown_contents:
#         if file_content is None:
#             continue
#         try:
#             for match in re.finditer(
#                 r'terraform\s+import\s+(azurerm_\w+)[^\n]*/providers/([^\s/]+(?:/[^/\s]+)*)',
#                 file_content['content'],
#                 re.IGNORECASE
#             ):
#                 tf_resource = match.group(1)
#                 provider_path = match.group(2).lower()
#                 if re.fullmatch(search_pattern, provider_path):
#                     azure_type = '/'.join(provider_path.split('/')[1:])
#                     matches.append((tf_resource, segments[0], azure_type))
#         except Exception as e:
#             print(f"Error processing {file_content.get('name', 'unknown')}: {e}")
#     return matches if matches else None

# def main():
#     try:
#         # 1. Fetch supported resources from CSV
#         resources = fetch_supported_resources()
        
#         # 2. Get markdown files from GitHub
#         print("Fetching markdown files from GitHub...")
#         markdown_files = fetch_github_files()
#         print(f"Found {len(markdown_files)} markdown files")
        
#         # 3. Download all markdown contents in parallel
#         with ThreadPoolExecutor(max_workers=8) as executor:
#             markdown_contents = list(filter(None, executor.map(get_markdown_content, markdown_files)))
        
#         # 4. Process resources against markdown contents
#         print("Searching for matching resources...")
#         with ThreadPoolExecutor(max_workers=8) as executor:
#             find_matches = partial(find_resource_matches, markdown_contents=markdown_contents)
#             results = list(filter(None, executor.map(find_matches, resources)))
        
#         # 5. Process and save results
#         flat_results = [item for sublist in results for item in sublist]
#         unique_results = sorted(set(flat_results), key=lambda x: x[0])
        
#         with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(["terraform_resource", "provider_name", "azure_resource_type"])
#             writer.writerows(unique_results)
            
#         print(f"\n✅ Found {len(unique_results)} matches. Results saved to {OUTPUT_FILE}")
        
#     except Exception as e:
#         print(f"\n❌ Error: {e}")
#         raise

# if __name__ == "__main__":
#     main()
