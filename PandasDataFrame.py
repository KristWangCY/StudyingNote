import pandas as pd
#Try to reseach function pandas.DataFrame(data, index, columns, dtype, copy)
#DataFrame is a 2 dimension array.
'''
data：一组数据(ndarray、series, map, lists, dict 等类型)。
index：索引值，或者可以称为行标签。
columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
dtype：数据类型。
copy：拷贝数据，默认为 False。
'''

# data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# df = pd.DataFrame(data, columns = ['Site', 'Age'], dtype = float)
# print(df)
# It doesn't work: ValueError: could not convert string to float: 'Google'


data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns = ['Site', 'Age'])
print(df)
print("\n")
#Output:
#     Site  Age
#0  Google   10
#1  Runoob   12
#2    Wiki   13


df['Age'] = df['Age'].astype(float)
#Alter the data type of column.
print(df)
print("\n")
#Output:
#     Site   Age
#0  Google  10.0
#1  Runoob  12.0
#2    Wiki  13.0


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print("\n")
#Output:
#   a   b     c
#0  1   2   NaN
#1  5  10  20.0
#Create DataFrame by Dictionary.
#Empty data will be shown as NaN.


import pandas as pd

data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
}
# Create DataFrame.
df = pd.DataFrame(data)
print(df)
print("\n")

print(df.loc[2])
print(df.loc[0])
print("\n")

print(df.loc[[1, 2]])
print("\n")

# Return data in one row by df.log().
# df.loc[x]: The value of return is (Series).
# df.loc[1,2]: The value of return is (Dataframe).
#Output:
#   calories  duration
#0       420        50
#1       380        40
#2       390        45


#calories    390
#duration     45
#Name: 2, dtype: int64
#calories    420
#duration     50
#Name: 0, dtype: int64


#   calories  duration
#1       380        40
#2       390        45


data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print("\n")
print(df.loc["day2"])#The original Index are replaced by the news.
print("\n")
Case = ["day1" , "day3"]
print(df.loc[Case])
# print(df.loc["day1", "day3"])
# It doesn't work.
# df.loc(self)

#Output:
#      calories  duration
#day1       420        50
#day2       380        40
#day3       390        45




