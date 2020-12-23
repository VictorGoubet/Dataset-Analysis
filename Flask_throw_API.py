from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json

app = Flask(__name__)



def treat_data(data):
    treated = pd.DataFrame.from_dict(data)


    treated = treated.drop(['Age',
                            'HoursPerWeek',
                            'MinimapRightClicks',
                            'ComplexUnitsMade',
                            'UniqueUnitsMade'],axis=1)

    for column in ['APM','TotalHours','ActionLatency','TotalMapExplored']:
        treated['log({})'.format(column)] = np.log(treated[column])
    

    treated = treated.to_numpy()
    return treated

@app.route('/api', methods=['POST'])
def makecalc():
    print("Let's Predict this players Index")
    data = request.get_json()
    treated = treat_data(data)
    
    prediction = np.array2string(model.predict(treated))
    return jsonify(prediction)

if __name__ == '__main__':

    modelfile = 'model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')