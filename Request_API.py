import requests
import json
import sklearn as sk
import sklearn.preprocessing 
import pandas as pd
import math as m

url = 'http://localhost:5000/api'

database = pd.read_csv("SkillCraft1_Dataset.csv", index_col="GameID")
data = database.drop("LeagueIndex", axis=1)

for col in ['Age', 'HoursPerWeek', 'TotalHours']:
    data[col] = pd.to_numeric(data[col], errors = 'coerce')

#And we set the nAn values to the mean : 
data.fillna(data.mean(), inplace=True)
#Chose the player you want to know the league Index predicted of : YOU CANT PUT IT [:]
to_predict = [60, 61, 72, 77, 81, 83, 93]
data = pd.DataFrame(data.loc[to_predict])


j_data = data.to_json()
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(type(r.text))
print(r, r.text)
res= r.text[2:-3].split(" ")
right = []
for i in range(len(to_predict)):
    if int(res[i]) == database.at[to_predict[i], 'LeagueIndex']:
        right.append(True)
    else:
        right.append(False)


print(right)