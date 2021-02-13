import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatues = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatues.append(row[1])


data = pandas.read_csv("weather_data.csv")
temp_list = data['temp']
avg_temp_list = sum(temp_list) / len(temp_list)
print("average temperature:", avg_temp_list)