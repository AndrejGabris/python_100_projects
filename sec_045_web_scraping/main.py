from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_title_tags = soup.select(selector=".titleline")
article_title_tags = soup.find_all(name="span", class_="titleline")


article_text = []
article_links = []

for tag in article_title_tags:
    text = tag.getText()
    article_text.append(text)

    link = tag.a.get("href")
    article_links.append(link)

article_upvote = [int(score.getText() .split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_text)
# print(article_links)
# print(article_upvote)

maximum_upvotes = article_upvote.index(max(article_upvote))


print(article_text[maximum_upvotes],"\n",article_links[maximum_upvotes],"\n",f"{article_upvote[maximum_upvotes]} points")