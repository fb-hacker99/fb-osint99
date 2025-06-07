#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

def extract_facebook_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; OSINT-Bot/1.0)'
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            print("[!] Failed to fetch the page. Status code:", r.status_code)
            return

        soup = BeautifulSoup(r.text, 'html.parser')

        og_title = soup.find("meta", property="og:title")
        og_desc = soup.find("meta", property="og:description")
        og_image = soup.find("meta", property="og:image")

        print("\n[+] OSINT Results for {}".format(url))
        print("Name         :", og_title["content"] if og_title else "N/A")
        print("Description  :", og_desc["content"] if og_desc else "N/A")
        print("Profile Photo:", og_image["content"] if og_image else "N/A")
        print("\n[!] Done.")

    except Exception as e:
        print("[!] Error occurred:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python2 facebook_osint.py <facebook_profile_url>")
        sys.exit(1)

    fb_url = sys.argv[1]
    if not fb_url.startswith("http"):
        fb_url = "https://facebook.com/irfan.jakaria.92" + fb_url

    extract_facebook_info(fb_url)
