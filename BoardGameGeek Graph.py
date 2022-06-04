import pandas
import matplotlib.pyplot as pyplot

username = input('Enter username to use collection file or leave blank to use BoardGameGeek Game Data.csv >> ')
if username == '':
    file = 'BoardGameGeek Game Data.csv'
else:
    file = username + ' BoardGameGeek Collection.'
try:
    csv_file = pandas.read_csv ('BoardGameGeek Game Data.csv', encoding = 'latin1')
    type = csv_file['Type']
    game = 0
    expansion = 0
    for item in type:
        if item == 'Game':
            game += 1
        if item == 'Expansion':
            expansion += 1
    pie_items = [game, expansion]
    labels = ["Games: " + str(game),"Expansions: " + str(expansion)]
    pyplot.pie(pie_items, labels=labels)
    pyplot.title("Game/Expansion Breakdown")
    pyplot.show()
except FileNotFoundError:
    print(file + ' not found')
