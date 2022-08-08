import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for i in article_tag:
    text = i.getText()
    link = i.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvote = [score.getText()
                  for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_upvote[0].split()[0])
# print(article_links)
