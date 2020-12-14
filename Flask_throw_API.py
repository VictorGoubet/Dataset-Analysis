from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def makecalc():
    print("Let's Predict this players Index")
    data = request.get_json()
    print(data)
    treated = pd.DataFrame.from_dict(data)


    treated = treated.drop(['Age',
                            'HoursPerWeek',
                            'MinimapRightClicks',
                            'ComplexUnitsMade',
                            'UniqueUnitsMade'],axis=1)

    treated['log(APM)']  = np.log(treated['APM'])
    treated['log(TotalHours)']  = np.log(treated['TotalHours'])
    treated['log(ActionLatency)']  = np.log(treated['ActionLatency'])
    treated['log(TotalMapExplored)']  = np.log(treated['TotalMapExplored'])


    treated = treated.to_numpy()

    
    prediction = np.array2string(model.predict(treated))
    return jsonify(prediction)

if __name__ == '__main__':

    modelfile = 'model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')