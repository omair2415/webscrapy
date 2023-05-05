#!/usr/bin/python3
import requests
import re

url = "https://books.toscrape.com/"
response = requests.get(url)

pattern = r'<a href="(.*?)">'
links = re.findall(pattern, response.text)

print(links)
