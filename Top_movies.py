from bs4 import BeautifulSoup
import requests

url="https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(url)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")
movie_section=soup.find_all('h2')
movie_titles=[]
for section in movie_section:
    strong_tag=section.find('strong')
    if strong_tag:
        movie_titles.append(strong_tag.get_text())
movies=movie_titles[::-1]

with open("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")