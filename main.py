import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_IMDB_info(movie_url):
    try:
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = str(soup.find_all(class_="text-link text-footer"))  

        tokens = text.split(" ")
        IMDB_id_token = tokens[8].split("/")[4]

        time_token = tokens[2]
        digit_buffer = ""
        for character in time_token:
            if character.isnumeric():
                digit_buffer += character
        time_token = digit_buffer

        return IMDB_id_token, time_token
    except:
        return 0

def converter(filelocation):
    df = pd.read_csv(filelocation)
    file = open("export.csv", "w")
    error_log = open("errors.log","w")
    counter = 0
    total_watch_time = 0

    file.write("Position,Const,Created,Modified,Description,Title,URL,Title Type,IMDb Rating,Runtime (mins),Year,Genres,Num Votes,Release Date,Directors,Your Rating,Date Rated\n")

    for url in df['Letterboxd URI']:
        response, time = get_IMDB_info(url)
        total_watch_time += int(time)
        if response == 0:
            print(f"Error in : {df['Name'][counter]} : {url}")
            error_string = "Error in : " + df['Name'][counter] + " - " + url + "\n"
            error_log.write(error_string)
        else:
            print(f"{df['Name'][counter]} : {response}: {time} done...")
            file.write(f"{counter + 1},{response},{df['Date'][counter]},{df['Date'][counter]},,{df['Name'][counter]},https://www.imdb.com/title/{response}/,movie,7.5,{response},{df['Year'][counter]},""Animation, Drama, Fantasy"",64368,2016-09-09,J.A. Bayona,,\n")

        counter += 1

    print(total_watch_time)
    file.close()
    error_log.close()
 


def main():
    converter('./tests/watched.csv')

main()