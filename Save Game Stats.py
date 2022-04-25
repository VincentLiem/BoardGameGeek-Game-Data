from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from pathlib import Path

game_list = input('Enter games seperated by "," >>')
game_list = (game_list .split(','))
browser=webdriver.Chrome()
browser.get('https://boardgamegeek.com/')
for game in game_list:
    search_bar = browser.find_element(By.NAME, 'searchTerm')
    search_bar.send_keys(game)
    search_bar.send_keys(Keys.ENTER)
    first_result = browser.find_element(By.CLASS_NAME, 'primary')
    first_result.click()
    game_name = browser.find_element(By.XPATH,'//h1')
    game_rank = browser.find_element(By.CLASS_NAME, 'rank-number')
    game_rating = browser.find_element(By.CLASS_NAME, 'ng-binding')
    game_name = game_name.text
    game_rank = game_rank.text
    game_rating = game_rating.text
    csv_file = Path('BoardGameGeek Game Data.csv')
    if csv_file.exists():
        with open('Yearly Cost.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow([game_name, game_rating, game_rank])
    else:
        with open('BoardGameGeek Game Data.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow(['Game Name', 'Rating', 'Rank'])                
            writer.writerow([game_name, game_rating, game_rank])
browser.quit
