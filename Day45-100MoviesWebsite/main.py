# 100MovieWebsite using Beautiful Soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.name)
# print(soup.prettify())

# print(soup.p)
