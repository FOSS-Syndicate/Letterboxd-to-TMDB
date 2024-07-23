import requests
from bs4 import BeautifulSoup
import pandas as pd

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

def converter(filelocation):
    df = pd.read_csv(filelocation)
    print(df.columns)
    file = open("export.csv", "w")
    error_log = open("errors.log","w")
    counter = 0

    for url in df['Letterboxd URI']:
        response = get_IMDB_id(url)
        if response == 0:
            print(f"Error in : {df['Name'][counter]} : {url}")
            error_string = "Error in : " + df['Name'][counter] + " - " + url + "\n"
            error_log.write(error_string)
        else:
            print(f"{response} + add to csv")
            file.write(f"")

        
        counter += 1
    
    file.close()
    error_log.close()
 


def main():
    converter('./tests/watched.csv')

main()