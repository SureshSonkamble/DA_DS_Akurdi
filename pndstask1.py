import pandas as pd
dt=pd.read_csv('studs.csv')
print("======python=====")
py=dt[dt['Course']=='Python']
print(py)
py.to_csv('py.csv')
print("=====All data=============")
print(dt)
print("========Attendance >90==========")
atnds=dt[dt['Attendance']>90]
print(atnds)
print("========Attendance <90==========")
atnds=dt[dt['Attendance']<90]
print(atnds)
print("========Above 90 marks==========")
mrk=dt[dt['Marks']>90]
print(mrk)
print("========female==========")
fml=dt[dt['Gender']=='Female']
print(fml)
fml.to_csv('female.csv')
print("========Male==========")
ml=dt[dt['Gender']=='Male']
print(ml)
ml.to_csv('male.csv')
print("success")




