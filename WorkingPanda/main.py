# import csv

# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
 #   tempe = []
 #   for row in data:
  #      if row[1] != "temp":
  #          tempe.append(int(row[1]))
  #          print(tempe)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)
#temp_list = data["temp"].to_list()
#print(temp_list)

#print(data["temp"].max())
#print(data["temp"].mean())

#maximo = data[data.temp == data.temp.max()]
#print(maximo)

#monday = data[data.day == "Monday"]
#monday_temp = int(monday.temp)

#fah = monday_temp * 9/5 + 32

#print(fah)

# create a dataframe from scratch

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")





