import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatues = []
    for row in data:
        if row[1] != 'temp':
            temperatues.append(row[1])
