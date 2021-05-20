from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"

response = requests.get(URL)
must_see_movies = response.text
soup = BeautifulSoup(must_see_movies, "html.parser")

entries = soup.select(selector="h3 a")

movie_titles = [entry.getText().strip() for entry in entries[:-1]]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in movie_titles:
        if "\xa0" in title:
            formatted_title = title.replace("\xa0", " ")
        file.write(f"{formatted_title}\n")
