from bs4 import BeautifulSoup
import urllib.request
import csv
import re

r= urllib.request.urlopen('https://www.census.gov/programs-surveys/popest.html').read()
soup = BeautifulSoup(r, "lxml")

all_url = []
for link in soup.find_all('a'):
    soup_link = str(link.get('href'))
    if "http" in soup_link:
        all_url.append(soup_link)
    elif soup_link.startswith("/"):
        all_url.append("https://www.census.gov"+ soup_link)

with open('parsed_data.csv', 'w+', newline='') as file:
    cleaned_url_list = []
    writer = csv.writer(file)
    for i in all_url:
        if i not in cleaned_url_list:
            cleaned_url_list.append(i)
            writer.writerow([i])
