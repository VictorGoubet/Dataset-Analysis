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

def predict(data):
    modelfile = './model.pickle'
    model = p.load(open(modelfile, 'rb'))
    data = preprocessing(data)
    return model.predict(data)
