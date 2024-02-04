# with open(r"sec_025_csv_us_states_game\weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)    




# import csv
# with open(r"sec_025_csv_us_states_game\weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)   



import pandas as pd

data = pd.read_csv(r"sec_025_csv_us_states_game\weather_data.csv")

# # dataframe -> to dicstionary
# data_dict = data.to_dict()
# print(data_dict)


# # pandas series -> list
# temp_list = data["temp"].to_list()
# print(temp_list)



# # average temperature
# print(data["temp"].mean())
# # maximum temperature
# print(data["temp"].max())



# # data in row
# print(data.condition)
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)



# # create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# data = pd.DataFrame(data_dict)
# print(data)
# # create a csv file
# data.to_csv(r"sec_025_csv_us_states_game\new_data.csv")


# ------------------------------------------------------------------------------------------------------------
# import pandas as pd
# squirrel_data = pd.read_csv(r"sec_025_csv_us_states_game\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240204.csv")
# print(squirrel_data.shape)
# p_f_c =squirrel_data["Primary Fur Color"].value_counts()
# p_f_c.to_csv(r"sec_025_csv_us_states_game\squirrel_count.csv")