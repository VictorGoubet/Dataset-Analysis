from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json


def preprocessing(data):
    data = pd.DataFrame.from_dict(data)

    # Drop data
    data.drop(['Age',
               'HoursPerWeek',
               'MinimapRightClicks',
               'ComplexUnitsMade',
               'UniqueUnitsMade'], axis=1, inplace=True)

    # Add log columns
    for column in ['APM', 'TotalHours', 'ActionLatency', 'TotalMapExplored']:
        data['log({})'.format(column)] = np.log(data[column])

    return data.to_numpy()


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def makecalc():
    print("Let's Predict theses players index")
    data = request.get_json()
    data = preprocessing(data)
    
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

if __name__ == '__main__':

    modelfile = './model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')