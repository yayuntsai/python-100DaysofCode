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
pan_avg_temp_list = temp_list.mean()
print("average temperature:", avg_temp_list)
print("average temperature (using pandas):", pan_avg_temp_list)