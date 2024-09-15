import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
eo_website = response.text

soup = BeautifulSoup(eo_website, "html.parser")
title_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
titles_list = [title.getText() for title in title_tags]

from_first_to_last = titles_list.reverse()

with open("sec_045_web_scraping\movies.txt",mode="w") as file:
    for title in titles_list:
        file.write(title)
        if title == titles_list[-1]:
            break
        file.write("\n")



