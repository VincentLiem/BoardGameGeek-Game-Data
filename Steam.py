from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from pathlib import Path

game_list = input('Enter games seperated by "|" >>')
game_list = (game_list .split('|'))
browser=webdriver.Chrome()
for game in game_list:
    browser.get('https://store.steampowered.com/')
    search_bar = browser.find_element(By.ID, 'store_nav_search_term')
    search_bar.send_keys(game)
    search_bar.send_keys(Keys.ENTER)
    first_result = browser.find_element(By.CLASS_NAME, 'title')
    game_name = browser.find_element(By.CLASS_NAME, 'title')
    game_name = game_name.text
    first_result.click()
    game_URL = browser.current_url
    release_date = browser.find_element(By.CLASS_NAME, 'date')
    recent_reviews = browser.find_element(By.CLASS_NAME, 'game_review_summary')
    recent_reviews = recent_reviews.text
    release_date = release_date.text
    csv_file = Path('Steam Game Date.csv')
    if csv_file.exists():
        with open('Steam Game Date.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow([game_name, release_date, recent_reviews, game_URL])
    else:
        with open('Steam Game Date.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow(['Game Name', 'Release Date', 'Recent Reviews', 'Steam URL'])                
            writer.writerow([game_name, release_date, recent_reviews, game_URL])
browser.quit
