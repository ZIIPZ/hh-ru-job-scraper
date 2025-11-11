thonimport json
import requests
from extractors.hh_parser import parse_job_listings
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def scrape_jobs():
    page = 1
    all_job_listings = []
    while True:
        search_url = f"{SETTINGS['base_url']}?text={SETTINGS['search_query']}&area=1&page={page}"
        response = requests.get(search_url, headers=SETTINGS['headers'])
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            break

        job_listings = parse_job_listings(response.text)
        if not job_listings:
            break

        all_job_listings.extend(job_listings)
        page += 1
    
    export_to_json(all_job_listings, SETTINGS['output_file'])

if __name__ == "__main__":
    scrape_jobs()