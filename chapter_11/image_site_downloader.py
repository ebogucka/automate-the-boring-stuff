#!/usr/bin/env python3
# Image Site Downloader
# Downloads top images from Imgur for a given search term.

import os
import sys
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: image_site_downloader.py <search_term>")
    sys.exit(1)

url = "https://imgur.com/search?q="
out_path = "img/"
os.makedirs(out_path, exist_ok=True)

# Get top results.
try:
    results = requests.get(url + " ".join(sys.argv[1:]))
    results.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    sys.exit(1)

soup = BeautifulSoup(results.text, features="html.parser")
links = soup.select("a.image-list-link")
# Visit each image's page.
for link in links:
    image_page_url = "https://imgur.com" + link.get("href")
    try:
        image_page = requests.get(image_page_url)
        image_page.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred when loading {image_page_url}: {http_err}")
        continue
    image_soup = BeautifulSoup(image_page.text, features="html.parser")
    image_src = image_soup.select('link[rel="image_src"]')
    if image_src:
        image_url = image_src[0].get("href")
        try:
            image = requests.get(image_url)
        except HTTPError as http_err:
            print(f"HTTP error occurred when downloading {image_url}: {http_err}")
            continue
        # Save the image.
        print(f"Downloading {image_url}...")
        try:
            with open(
                os.path.join(out_path, os.path.basename(image_url)), "wb"
            ) as image_file:
                for chunk in image.iter_content(100_000):
                    image_file.write(chunk)
        except OSError as err:
            print(str(err))
            continue
        except IOError as err:
            print(str(err))
            continue
