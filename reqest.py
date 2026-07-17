    import requests
import pandas as pd
url="https://api.rootnet.in/covid19-in/stats/latest"
rs=requests.get(url)
data=rs.json()
#print(data)
#json parsing
print(data['data']['summary']['total'])
print(data['data']['summary']['confirmedCasesIndian'])
print(data['data']['summary']['confirmedCasesForeign'])
print(data['data']['summary']['discharged'])
print(data['data']['summary']['deaths'])
l=len(data['data']['regional'])
print("Length:=",l)
print(data['data']['regional'][0]['loc'])
cnt=0
sts=[]
cse=[]
fl=open('sts.txt','a')
for i in range(l):

    dt=data['data']['regional'][i]['loc']
    fl.write((dt+"\n"))
    #print(data['data']['regional'][i]['loc']," | ",data['data']['regional'][i]['confirmedCasesIndian'])
    if(data['data']['regional'][i]['totalConfirmed']<100000):
        sts.append(data['data']['regional'][i]['loc'])
        cnt=cnt+1
    
    if(data['data']['regional'][i]['deaths']<100):
        print(print(data['data']['regional'][i]['loc']))
fl.close()
print("file write success..")             
print("Total count <100000:=",cnt)









