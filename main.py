import pandas
file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(file[file["Primary Fur Color"] == "Gray"])
cinnamon_count = len(file[file["Primary Fur Color"] == "Cinnamon"])
black_count = len(file[file["Primary Fur Color"] == "Black"])
squirrel_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")
