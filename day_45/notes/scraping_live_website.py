from bs4 import BeautifulSoup
import requests

# Scraping from https://news.ycombinator.com/

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_votes = max(article_upvotes)
most_voted_index = article_upvotes.index(most_votes)

print(article_texts[most_voted_index])
print(article_links[most_voted_index])
