import requests
from bs4 import BeautifulSoup
import datetime


#input_date = input("Enter wayback date (YYYY-MM-DD): ")

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

all_hr = soup.find_all("hr")
for hr in all_hr:
    if len(hr.contents)==2:
        print(len(hr.contents[1]))
# top_list = [song.get_text() for song in soup.select("span", class_="c-level")]
# print(top_list)

# company = soup.select("#title-of-a-story")[0].text.strip()
# print(company)
#
# c = soup.select('span.c-label')[0].text.strip()
# print(c)

# d = soup.select('div.o-chart-results-list-row-container')
# print(d)