import requests
import json
import sklearn as sk
import sklearn.preprocessing 
import pandas as pd
import math as m

def get_response_request(data):
    url = 'http://localhost:5000/API_request'
    # Convert in json
    j_data = json.dumps(data)
    # Send request
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers).text
    r = list(map(int, r[2:-3].split(' ')))
    return r

if __name__ == '__main__':
    # Example of sended data (here 2 rows)
    data = {'Age':[21, 56],
            'HoursPerWeek': [256, 6],
            'TotalHours': [15, 2],
            'APM': [54 ,23.5],
            'SelectByHotkeys': [85.3, 0.3],
            'AssignToHotkeys': [85.3, 1],
            'UniqueHotkeys': [1, 3],
            'MinimapAttacks': [7, 6],
            'MinimapRightClicks': [85 ,33], 
            'NumberOfPACs': [7, 3],
            'GapBetweenPACs': [1, 1],
            'ActionLatency': [5, 0.2],
            'ActionsInPAC': [0.9, 6],
            'TotalMapExplored': [7, 9],
            'WorkersMade': [3, 6],
            'UniqueUnitsMade': [152, 363],
            'ComplexUnitsMade': [59, 62],
            'ComplexAbilitiesUsed': [5, 6]}
    response = get_response_request(data)
    for i, pred in enumerate(response):
        print(f'Prediction {i+1}: {pred}')


