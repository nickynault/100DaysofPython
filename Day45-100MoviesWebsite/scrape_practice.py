import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
article_tag = soup.select_one(".titleline a")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score")

print(article_text)
print(article_link)
print(article_upvote.getText())

# Do it again but for all of them
articles = soup.select(".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

# Find most upvoted article
largest_num = max(article_upvotes)
largest_index = article_upvotes.index(largest_num)

print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_num)
