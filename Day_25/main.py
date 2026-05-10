# with open("weather_data.csv", "r") as data:
#     print(data.readlines())

# import csv
# with open("./weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["day"])
print(data["temp"])
print(data["condition"])