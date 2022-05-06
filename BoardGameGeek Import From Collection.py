from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
from pathlib import Path
from BoardGameGeek import *

username = input('Enter BoardGameGeek username >> ')
browser=webdriver.Chrome()
browser.get('https://boardgamegeek.com/collection/user/' + username)

game_links = []
links = browser.find_elements(By.TAG_NAME, 'a.primary')

for link in links:
    link = link.get_attribute("href")
    if str(link).find('https://boardgamegeek.com/boardgame/') != -1 or str(link).find('https://boardgamegeek.com/boardgameexpansion/') != -1:
        game_links.append(link)
for game in game_links:
    driver(game)
    scrape_game_page()

    csv_file = Path(username + ' BoardGameGeek Collection.csv')
    if csv_file.exists():
        with open(username + ' BoardGameGeek Collection.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            write_fields(writer)
    else:
        with open(username + ' BoardGameGeek Collection.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow(['Game Name', 'Type', 'Rating', 'Rank', 'Weight', 'Play Time', 'Player Count','Recommended Player Count', 'BGG URL'])                
            write_fields(writer)
            
browser.quit
