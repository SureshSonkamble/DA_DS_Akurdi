import pandas as pd
#data=pd.read_csv('covid.csv')
#print(data)
data=pd.read_excel('cvd.xlsx')
print(data)
#Inspect function
print(data.info())#info about excel
print(data.head())#first 5 data
print(data.tail())#last 5 data
print(data.dtypes)
print(data.columns)
print(data.shape)#(36X3)

