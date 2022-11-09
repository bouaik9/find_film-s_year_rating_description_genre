import requests
from bs4 import BeautifulSoup

films = []
name = input("Enter film name : ").lower()
search = "+".join(name.split())

url = "https://www.imdb.com/search/title/?title="+search
response = requests.get(url).text

soup = BeautifulSoup(response,"html.parser")
second_soup = soup.find_all("div", class_="lister-item-content")

for result in second_soup:
    film_name = result.h3.a.text
    film_year = result.h3.find("span", class_="lister-item-year text-muted unbold").text
    film_genre = result.p.find("span", class_="genre").text
    film_description = result.find_all("p", class_="text-muted")[1].text
    try:
        film_rate = result.strong.text
    except:
        film_rate = "not available"
    name11 = str(film_name).lower()
    if name == name11:
        object = ("---"+name11 + str(film_year))+"\ngenre:"+str(film_genre)+"\nDescription:"+str(film_description)+"\nrating:"+str(film_rate)
        films.append(object)

for one in films:
    print(one)

