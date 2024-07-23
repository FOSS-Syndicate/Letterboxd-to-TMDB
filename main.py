import requests
from bs4 import BeautifulSoup

def calc(movie_url):
    try:
        response = requests.get("https://boxd.it/chpK")
        soup = BeautifulSoup(response.content, 'html.parser')
        text = str(soup.find_all(class_="text-link text-footer"))
        text3 = text.find_all()   

        print(text)

        tokens = text.split(" ")
        time_token = tokens[2]
        digit_buffer = ""
        for character in time_token:
            if character.isnumeric():
                digit_buffer += character

        return int(digit_buffer)
    
    except:
        return 0
    
print(calc("hello"))