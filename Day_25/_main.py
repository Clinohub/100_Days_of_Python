# # with open("weather_data.csv", "r") as data:
# #     print(data.readlines())
#
# # import csv
# # with open("./weather_data.csv", "r") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         print(row)
# #         if not row[1] == "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # print("Average temperature:", sum(data["temp"].to_list())/len(data["temp"].to_list()))
# # print("Average temperature:", data["temp"].mean())
# # print()
# #
# # print("Max temp:", data["temp"].max())
# # print("Max temp:", max(data["temp"].to_list()))
# # print()
#
# # monday_row = data[data["day"] == "Monday"]
# # print(monday_row.temp  * 9/5 + 32)
#
#
#
# # DataFrame
# import pandas
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("./students_scores.csv")
#

#import math
import pandas

squirrel_census = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260510.csv")

fur_colors = {
    "Fur Color": [],
    "Count": []
}
for fur_color in squirrel_census["Primary Fur Color"]:
    if type(fur_color) == str:
        if fur_color not in fur_colors["Fur Color"]:
            fur_colors["Fur Color"].append(fur_color)

for i in range(len(fur_colors["Fur Color"])):
    fur_colors["Count"].append(0)

colour_count = 0
l = 0
for color in fur_colors["Fur Color"]:
    for k in squirrel_census["Primary Fur Color"]:
        if k == color:
            colour_count += 1

    fur_colors["Count"][l] = colour_count
    l += 1
    colour_count = 0

squirrel_count = pandas.DataFrame(fur_colors)
squirrel_count.to_csv("./squirrel_count.csv")