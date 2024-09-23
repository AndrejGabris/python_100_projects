import requests
from bs4 import BeautifulSoup
from datetime import datetime



date_format = '%Y-%m-%d'
today_date = datetime.now()
date_dt = today_date

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
error_ocured = True
is_program_on = True

while error_ocured and is_program_on:
    if date == "Y" or date == "y":
            is_program_on = False
    else:
        try:
            date_dt = datetime.strptime(date, date_format)
            date_splited = date.split("-")
            
            if (len(date_splited[0]) != 4) or (len(date_splited[1]) != 2) or (len(date_splited[2]) != 2):
                date = input("You wrote a date in wrong format (YYYY-MM-DD) or a future date. Try again :) \nIf you want to leave this script type [Y]:\n")
                error_ocured = True
            elif date_dt >= today_date:
                date = input("You wrote a date in wrong format (YYYY-MM-DD) or a future date. Try again :) \nIf you want to leave this script type [Y]:\n")
                error_ocured = True
            else: 
                response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
                billboard_web_page = response.text
                

                soup = BeautifulSoup(billboard_web_page, 'html.parser')
                song_titles_tags = soup.select(selector='li ul li h3')
                song_titles = []
                for song_title in song_titles_tags:
                    song_title_text = song_title.getText().strip()
                    song_titles.append(song_title_text)

                print(song_titles)

                error_ocured = False
        except ValueError:
            date = input("You wrote a date in wrong format (YYYY-MM-DD) or a future date. Try again :) \nIf you want to leave this script type [Y]:\n")
            error_ocured = True
            



# while date_dt >= today_date:
#     try:
#         date_dt = datetime.strptime(date, date_format)
#     except ValueError:
#         date = input("You wrote a date in wrong format (YYYY-MM-DD) or future date. Try again :) \nIf you want to leave this script type [Y]:\n")
    
#     if date == "Y" or "y":
#         break
   
    



# response = requests.get("")
# billboad_web_page = response.text


# soup = 