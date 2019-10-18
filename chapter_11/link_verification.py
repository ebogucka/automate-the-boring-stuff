#!/usr/bin/env python3
# Link Verification - verifies all links on a given webpage

import sys
from bs4 import BeautifulSoup
import requests

if len(sys.argv) < 2:
    print("Usage: link_verification.py <url>")
    sys.exit(1)

try:
    webpage = requests.get(sys.argv[1])
    webpage.raise_for_status()
except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as http_err:
    print(f"Failed to load the webpage: {http_err}")
    sys.exit(1)

soup = BeautifulSoup(webpage.text, features="html.parser")
links = soup.select("a")
print("Broken links:")
for link in links:
    try:
        url = link.get("href")
        if not url or not url.startswith("http"):
            continue
        linked_page = requests.get(link.get("href"))
        linked_page.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(http_err)
    except requests.exceptions.MissingSchema as schema_err:
        print(schema_err)
print("Done!")
