import pandas as pd
import json
import numpy as np

w = pd.read_csv('weather_data.csv')

# w is the data frame
#print(type(w))
# column name is the series, like a list 
#print(type(w["temp"]))

# you can convert a df into a dictionary
# data_dict = w.to_dict()
# print(data_dict)

# temp_list = w["temp"].to_list()
# print(temp_list)

# get row of data with highest temp
#by column
# maxtemp = w.max()
# print(maxtemp)

#by row
# maxx = (w[w.temp == w.temp.max()])
# print(maxx)

# get specific rows with the given temp
# f = w.loc[w['temp'] == 14]

#get Monday temp and convert to farenheit
# mon = w[w.day == "Monday"].temp.item()
# f = mon * 9/5 + 32
# print(f)


#ways of calling column
print(w["condition"])



