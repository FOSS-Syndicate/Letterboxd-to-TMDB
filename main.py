import requests
from bs4 import BeautifulSoup

def calc(movie_url):
    try:
        response = requests.get("https://boxd.it/chpK")
        soup = BeautifulSoup(response.content, 'html.parser')
        text = str(soup.find_all(class_="text-link text-footer"))  

        tokens = text.split(" ")
        IMDB_token = tokens[8].split("/")
        
        print(IMDB_token)


        return int(digit_buffer)
    
    except:
        return 0
    
print(calc("hello"))