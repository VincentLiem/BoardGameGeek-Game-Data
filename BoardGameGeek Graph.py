import pandas
import matplotlib.pyplot as pyplot

def game_expansion_breakdown(csv_file):
    type = csv_file['Type']
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

def weight_breakdown(csv_file):
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

def year_breakdown(csv_file):
    csv_years = csv_file['Year']
    csv_years_list = []
    for year in csv_years:
            csv_years_list.append(year)
    csv_years_list.sort()
    years_with_item = []
    for year in csv_years_list:
        if year not in years_with_item:
            years_with_item.append(year)
    bar_items = []
    for item in years_with_item:
        bar_items.append(0)
    for item in csv_years_list:
        if item in years_with_item:
            position = years_with_item.index(item)
            bar_items[position] += 1
    labels = years_with_item
    pyplot.bar(labels, bar_items)
    pyplot.xlabel('Year')
    pyplot.ylabel('Number of Games')
    pyplot.title('Year Breakdown')
    pyplot.show()

if __name__ == '__main__':
    username = input('Enter username to use collection file or leave blank to use BoardGameGeek Game Data.csv >> ')
    if username == '':
        file = 'BoardGameGeek Game Data.csv'
    else:
        file = username + ' BoardGameGeek Collection.csv'
    try:
        csv_file = pandas.read_csv (file, encoding = 'latin1')
        game_expansion_breakdown(csv_file)
        weight_breakdown(csv_file)
        year_breakdown(csv_file)
    except FileNotFoundError:
        print(file + ' not found')
