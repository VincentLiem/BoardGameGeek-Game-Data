from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
from pathlib import Path

def write_fields(x):
    x.writerow([game_name, type, game_rating, game_rank, weight, play_time, player_count, recomended_player_count, game_URL])

game_list = input('Enter games seperated by "|" >> ')
game_list = (game_list .split('|'))
browser=webdriver.Chrome()

for game in game_list:
    browser.get('https://boardgamegeek.com/')
    search_bar = browser.find_element(By.NAME, 'searchTerm')
    search_bar.send_keys(game)
    search_bar.send_keys(Keys.ENTER)
    try:
        first_result = browser.find_element(By.CLASS_NAME, 'primary')
        first_result.click()
        game_URL = browser.current_url
        type == 'N/A'
        if str(game_URL).find('https://boardgamegeek.com/boardgame/') != -1:
            type = "Game"
        if str(game_URL).find('https://boardgamegeek.com/boardgameexpansion/') != -1:
            type = "Expansion"
        game_name = browser.find_element(By.CSS_SELECTOR, 'h1>a[class="ng-binding"]')
        try:
            game_rank = browser.find_element(By.CSS_SELECTOR, 'a[class="rank-value ng-binding ng-scope"]')
            game_rank = game_rank.text
        except NoSuchElementException:
            game_rank = 'N/A'
        game_rating = browser.find_element(By.CSS_SELECTOR, 'span[ng-show="showRating"]')
        player_count = browser.find_element(By.CLASS_NAME, 'gameplay-item-primary')
        recomended_player_count = browser.find_element(By.CLASS_NAME, 'gameplay-item-secondary')
        play_time = browser.find_element(By.CLASS_NAME, 'gameplay-item:nth-child(2)')
        weight = browser.find_element(By.CLASS_NAME, 'gameplay-item:nth-child(4)')
        game_name = game_name.text
        game_rating = game_rating.text
        player_count=player_count.text
        recomended_player_count=recomended_player_count.text
        play_time = play_time.text
        weight = weight.text
        play_time = play_time.split('\n', 1)[0]
        weight = weight.split('\n', 1)[0]
        weight = weight.replace('Weight: ','')
        csv_file = Path('BoardGameGeek Game Data.csv')
        if csv_file.exists():
            with open('BoardGameGeek Game Data.csv', 'a',newline='') as save:
                writer = csv.writer(save)
                write_fields(writer)
        else:
            with open('BoardGameGeek Game Data.csv', 'a',newline='') as save:
                writer = csv.writer(save)
                writer.writerow(['Game Name', 'Type', 'Rating', 'Rank', 'Weight', 'Play Time', 'Player Count','Recommended Player Count', 'BGG URL'])               
                write_fields(writer)
    except NoSuchElementException:
         print(game + ' not found, skipped')

browser.quit
