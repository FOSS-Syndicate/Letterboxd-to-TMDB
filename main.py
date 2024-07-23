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
    # f = open("export.txt", "w")
    # error_log = open("errors.log","w")
    # counter = 0
    # total_minutes = 0

    for url in df['Letterboxd URI']:
        response = get_IMDB_id(url)
        if response == 0:
            print("ERROR")
        else:
            print(f"{response} + add to csv")    
    #     time.sleep(2)
    #     movie_time = calc(url)
    #     total_minutes += movie_time
    #     print(df['Name'][counter] + " : " + str(movie_time) + " minutes")

    #     if movie_time == 0:
    #         error_string = "Error in : " + df['Name'][counter] + " - " + url + "\n"
    #         error_log.write(error_string)
    #         listbox.insert(counter + 2, error_string)
    #     else:
    #         output_string = df['Name'][counter] + " : " + str(movie_time) + " minutes\n"
    #         f.write(output_string)
    #         listbox.insert(counter + 2,  output_string)

    #     counter += 1

    # f.write(f"\nTotal movie watchtime in minutes : {total_minutes}\n")
    # f.write(f"Total movie watchtime in hours : {total_minutes / 60}\n")
    # listbox2.insert(2, f"Total movie watchtime in minutes : {total_minutes}\n")
    # listbox2.insert(3, f"Total movie watchtime in hours : {total_minutes / 60}\n")

    # f.close()
    # error_log.close()
    # messagebox.showinfo("Success", "Done Processing") 


def main():
    converter('./tests/watched.csv')

main()