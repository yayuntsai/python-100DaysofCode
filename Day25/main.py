import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatues = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatues.append(row[1])


### Practice pandas
data = pandas.read_csv("weather_data.csv")
temp_list = data['temp']
avg_temp_list = sum(temp_list) / len(temp_list)
pan_avg_temp_list = temp_list.mean()
#print("average temperature:", avg_temp_list)
##print("Highest temperature: ", data[data.temp == max_temp])



### Open data practice
park_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(park_data[park_data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(park_data[park_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(park_data[park_data['Primary Fur Color'] == 'Black'])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
print(df.to_csv("squirrel.csv"))

# count_gray = 0
# count_cinnamon = 0
# for item in color_list:
#     if item == 'Gray':
#         count_gray += 1
#     elif item == 'Cinnamon':
#         count_cinnamon += 1







#gray = park_data['Primary Fur Color' == 'Gray'].count()
count_table = color_list.set_index(["Primary Fur Color"]).count(level="Primary Fur Color")
print(count_table)

