import pandas as pd
dt=pd.read_csv('studs.csv')


'''print("=====All data=============")
print(dt)
print("=====# 1. Remove duplicate rows===")
df = dt.drop_duplicates("Name")
print(df)
print("# 2. Remove rows with any empty cell")
df = dt.dropna()
print(df)
print("======atnds between 50 to 70")
bt=dt[dt['Attendance'].between(50,70)]
print(bt)
print("=====female & attendance >90=============")
fmlantds=dt[(dt['Attendance']>90) & (dt['Gender']=='Female')]
print(fmlantds)
print("==========male & java=============")
mljava=dt[(dt['Gender']=='Male')&(dt['Course']=='Java')]
print(mljava)
print("==========male & java & pune=============")
mljava=dt[(dt['Gender']=='Male')&(dt['Course']=='Java')&(dt['City']=='Pune')]
print(mljava)'''
