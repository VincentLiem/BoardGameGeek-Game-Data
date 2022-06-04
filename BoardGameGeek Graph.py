import pandas
import matplotlib.pyplot as pyplot

username = input('Enter username to use collection file or leave blank to use BoardGameGeek Game Data.csv >> ')
if username == '':
    file = 'BoardGameGeek Game Data.csv'
else:
    file = username + ' BoardGameGeek Collection.csv'
try:
    csv_file = pandas.read_csv (file, encoding = 'latin1')
    type = csv_file['Type']
    #Game/Expansion Breakdown
    game = 0
    expansion = 0
    for item in type:
        if item == 'Game':
            game += 1
        if item == 'Expansion':
            expansion += 1
    pie_items = [game, expansion]
    labels = ['Games: ' + str(game),'Expansions: ' + str(expansion)]
    pyplot.pie(pie_items, labels=labels)
    pyplot.title('Game/Expansion Breakdown')
    pyplot.show()
    #Weight Breakdown
    csv_file_expansion_removed = csv_file[csv_file['Type'] == 'Game']
    weight_one = 0
    weight_two = 0
    weight_three = 0
    weight_four = 0
    weight = csv_file_expansion_removed['Weight']
    for item in weight:
        item = item.split('/')[0]
        if float(item) >=4:
            weight_four += 1
        elif float(item) >=3:
            weight_three += 1
        elif float(item) >=2:
            weight_two += 1
        elif float(item) >=1:
            weight_one+= 1
    bar_items = [weight_one,weight_two,weight_three,weight_four]
    labels = ['1','2','3','4']
    pyplot.bar(labels, bar_items)
    pyplot.xlabel('Weight')
    pyplot.ylabel('Number of Games')
    pyplot.title('Weight Breakdown')
    pyplot.show()
except FileNotFoundError:
    print(file + ' not found')
