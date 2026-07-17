import pandas as pd
import requests
url="https://api.rootnet.in/covid19-in/stats/latest"
rs=requests.get(url)
data=rs.json()
l=len(data['data']['regional'])
print("Length:=",l)
nm=[]
ttl=[]  
for i in range(l):
    nm.append(data['data']['regional'][i]['loc'])
    ttl.append(data['data']['regional'][i]['totalConfirmed'])
#1.list
'''nm=['suresh','ramesh','jayesh']
mob=['8485070453','8308357068','8485070453']
ct=['nashik','nashik','nashik']'''
#2.dic
dic={
     "Name":nm,
     "Total":ttl
    }
print(dic)
#3.dataframe
df=pd.DataFrame(dic)
print(df)
#4.csv
df.to_excel('cvd.xlsx')
df.to_csv("covid.csv")
print("success")
