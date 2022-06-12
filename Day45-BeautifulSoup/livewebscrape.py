# web scraping using live website
# gathering all title, url and upvoted article - I used list comprehension.
# get the highest upvoted news

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
news = soup.find_all("a", class_="titlelink")

links = [l.get("href") for l in soup.find_all("a", class_="titlelink")]

texts = [t.get_text() for t in soup.find_all("a", class_="titlelink")]

votes = [int(v.get_text().split()[0]) for v in soup.find_all("span", class_="score")]
print(votes)

max_indx = votes.index(max(votes))
#print(max_indx, links[max_indx], texts[max_indx])
