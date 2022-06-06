import pandas
import matplotlib.pyplot as pyplot

def pie_chart(csv_file):
    item_name = csv_file['Item Name']
    yearly_cost = csv_file['Yearly Cost']

    total_cost = 0
    for item in yearly_cost:
        total_cost += item

    percentage_list = []
    for item in yearly_cost:
        percentage = item / total_cost * 100
        percentage = format(percentage, '.2f')
        percentage_list.append(percentage)

    string_yearly_cost =[]
    for item in yearly_cost:
        item = format(item, '.2f')
        item = str(item)
        string_yearly_cost.append(item)

    pyplot.pie(yearly_cost, labels = item_name + ': $' + string_yearly_cost + '\n' + percentage_list + '%')
    pyplot.title("Breakdown of Costs")
    pyplot.show()

def bar_graph(csv_file):
    item_name = csv_file['Item Name']
    yearly_cost = csv_file['Yearly Cost']

    pyplot.bar(item_name, yearly_cost)
    pyplot.title("Breakdown of Costs")
    pyplot.xlabel = ('Cost Name')
    pyplot.ylabel = ('Yearly Cost')
    pyplot.show()

if __name__ == '__main__':
    try:
        csv_file = pandas.read_csv ('Yearly Cost.csv')
        pie_chart(csv_file)
        bar_graph(csv_file)
    except FileNotFoundError:
        print("Yearly Cost.csv not created yet")
