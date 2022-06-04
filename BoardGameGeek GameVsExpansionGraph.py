import pandas
import matplotlib.pyplot as pyplot

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
    pyplot.title("Game/Expansion breakdown")
    pyplot.show()
except FileNotFoundError:
    print("BoardGameGeek Game Data.csv not created yet")