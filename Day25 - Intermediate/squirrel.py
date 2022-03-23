#Get squirrel primary colors and count them

import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cin_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
blk_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])


df = pd.DataFrame({'fur_color': ["Gray", "Cinnamon", "Black"],
                'count': [gray_squirrels, cin_squirrels, blk_squirrels]})
print(df)

