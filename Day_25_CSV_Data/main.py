import pandas
data = pandas.read_csv("./Day_25_CSV_Data/2018_Central_Park_Squirrel.csv")
num_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_of_black = len(data[data["Primary Fur Color"] == "Black"])
num_of_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(num_of_gray)
print(num_of_black)
print(num_of_cinnamon)
my_dict = {"Color":["Gray", "Black", "Cinnamon"],
           "number":[num_of_gray,num_of_black,num_of_cinnamon]
           }
dt = pandas.DataFrame(my_dict)
dt.to_csv("./Day_25_CSV_Data/new_table.csv")