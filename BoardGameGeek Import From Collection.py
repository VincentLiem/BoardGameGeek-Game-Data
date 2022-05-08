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
browser.quit()

for game in game_links:
    OpenSite(game)
    ScrapeGamePage()
    AddToCSV(username + ' BoardGameGeek Collection.csv')

browser.quit()
