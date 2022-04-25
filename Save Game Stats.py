from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

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
time.sleep(13)
browser.quit