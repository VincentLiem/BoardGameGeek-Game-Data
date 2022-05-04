from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
from pathlib import Path

def write_fields(x):
    x.writerow([game_name, game_rating, game_rank, weight, play_time, player_count, recomended_player_count, game_URL])

username = input('Enter BoardGameGeek username >> ')
browser=webdriver.Chrome()
browser.get('https://boardgamegeek.com/collection/user/' + username)

game_links = []
links = browser.find_elements(By.TAG_NAME, 'a.primary')

for link in links:
    link = link.get_attribute("href")
    if str(link).find('https://boardgamegeek.com/boardgame/') != -1:
        game_links.append(link)

for game in game_links:
    browser.get(game)
    game_URL = browser.current_url
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
    csv_file = Path(username + ' BoardGameGeek Collection.csv')
    if csv_file.exists():
        with open(username + ' BoardGameGeek Collection.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            write_fields(writer)
    else:
        with open(username + ' BoardGameGeek Collection.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow(['Game Name', 'Rating', 'Rank', 'Weight', 'Play Time', 'Player Count','Recommended Player Count', 'BGG URL'])                
            write_fields(writer)
            
browser.quit