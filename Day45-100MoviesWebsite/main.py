# 100MovieWebsite using Beautiful Soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup

response = requests.get("https://empireonline.com/movies/features/best-movies-2")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
movie_titles = [title.getText() for title in soup.find_all("h3")]
movie_titles.reverse()
print(movie_titles)

with open("output.txt", "w", encoding="utf-8") as file:
    for item in movie_titles:
        file.write(str(item) + '\n')
