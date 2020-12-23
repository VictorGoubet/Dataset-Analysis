import requests
import json
import sklearn as sk
import sklearn.preprocessing 
import pandas as pd
import math as m

url = 'http://localhost:5000/api'

def get_data():
    # Import data to predict
    data = pd.read_csv("./SkillCraft1_Dataset.csv", index_col="GameID")
    data.drop("LeagueIndex", axis=1, inplace=True)

    # Make appropriate convertions
    for col in ['Age', 'HoursPerWeek', 'TotalHours']:
        data[col] = pd.to_numeric(data[col], errors = 'coerce')

    # Set the NaN values to the mean : 
    data.fillna(data.mean(), inplace=True)

    # Chose the player you want to know the predicted league Index:
    to_predict = [60, 61, 72, 77, 81, 83, 93]
    data = pd.DataFrame(data.loc[to_predict])
    return data

# Convert in json
j_data = get_data().to_json()

# Send request
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)

print("Response: ", r.text)