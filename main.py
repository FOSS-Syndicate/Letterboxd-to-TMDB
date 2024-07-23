import requests
from bs4 import BeautifulSoup

def get_IMDB_id(movie_url):
    try:
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = str(soup.find_all(class_="text-link text-footer"))  

        tokens = text.split(" ")
        IMDB_id_token = tokens[8].split("/")[4]

        return IMDB_id_token
    except:
        return 0

def main():
    print(get_IMDB_id("https://boxd.it/chpK"))

main()