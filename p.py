

import os
import re
import csv
import requests
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# Configuration for GitHub repository
GITHUB_OWNER = "hashicorp"
GITHUB_REPO = "terraform-provider-azurerm"
GITHUB_PATH = "website/docs/r"  # Directory where the markdown files are located
OUTPUT_FILE = "terraform_resources_with_tags.csv"
CSV_URL = "https://raw.githubusercontent.com/tfitzmac/resource-capabilities/main/tag-support.csv"

def fetch_supported_resources():
    """Fetch supported resources that support tags from a CSV file on GitHub"""
    try:
        response = requests.get(CSV_URL, timeout=10)
        response.raise_for_status()
        reader = csv.DictReader(response.text.splitlines())
        supported_resources = []
        for row in reader:
            if row.get('supportsTags', '').strip().upper() == 'TRUE':
                provider = row['providerName'].replace(" ", ".").lower()
                resource_type = row['resourceType']
                supported_resources.append(f"{provider}/{resource_type}")
        print(f"Found {len(supported_resources)} resources supporting tags")
        return supported_resources
    
    except Exception as e:
        print(f"Error fetching CSV: {e}")
        raise

def get_markdown_files():
    """Fetch all .markdown files from the GitHub repository's website/docs/r directory"""
    api_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_PATH}"
    response = requests.get(api_url)
    response.raise_for_status()

    markdown_files = []
    for item in response.json():
        if item["name"].endswith(".markdown"):
            file_url = item["download_url"]
            file_response = requests.get(file_url)
            file_response.raise_for_status()
            markdown_files.append((item["name"], file_response.text))

    if not markdown_files:
        raise FileNotFoundError(f"No markdown files found in {GITHUB_PATH}")
    
    return markdown_files

def find_resource_matches(resource, markdown_files):
    """Find matching Terraform resources for a given Azure resource in the markdown files"""
    segments = resource.split('/')
    search_pattern = re.escape(segments[0].lower())
    
    for segment in segments[1:]:
        if not segment or ' ' in segment:
            return None
        search_pattern += r'/[^/]+'
    
    matches = []
    for md_file, content in markdown_files:
        try:
            for match in re.finditer(
                r'terraform\s+import\s+(azurerm_\w+)[^\n]*/providers/([^\s/]+(?:/[^/\s]+)*)',
                content,
                re.IGNORECASE
            ):
                tf_resource = match.group(1)
                provider_path = match.group(2).lower()
                if re.fullmatch(search_pattern, provider_path):
                    azure_type = '/'.join(provider_path.split('/')[1:])
                    matches.append((tf_resource, segments[0], azure_type))
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    return matches if matches else None

def main():
    try:
        # Fetch supported resources
        resources = fetch_supported_resources()

        # Get the markdown files from GitHub
        markdown_files = get_markdown_files()

        print(f"Searching {len(markdown_files)} markdown files...")

        # Process in parallel
        with ThreadPoolExecutor(max_workers=8) as executor:
            find_matches = partial(find_resource_matches, markdown_files=markdown_files)
            results = list(filter(None, executor.map(find_matches, resources)))
        
        # Flatten and deduplicate results
        flat_results = [item for sublist in results for item in sublist]
        unique_results = sorted(set(flat_results), key=lambda x: x[0])

        # Save the results to a CSV file
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["terraform_resource", "provider_name", "azure_resource_type"])
            writer.writerows(unique_results)

        print(f"\n✅ Total {len(unique_results)} resources saved to {OUTPUT_FILE}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        if isinstance(e, FileNotFoundError):
            print(f"GitHub directory path: {GITHUB_PATH}")
        raise

if __name__ == "__main__":
    main()

