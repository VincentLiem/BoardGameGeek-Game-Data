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
browser.quit

for game in game_links:
    driver(game)
    scrape_game_page()
    add_to_csv(username + ' BoardGameGeek Collection.csv')
