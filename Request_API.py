import requests
import json
import sklearn as sk
import sklearn.preprocessing 

url = 'http://0.0.0.0:5000/api/'

data = [[1,84.7086,0.0011134377,8.30923654734603e-05,2,0.0002409679,
0.0003988434,0.0031242729,48.512,62.6064,4.5585,25,0.0012547,
7,4.15461827367302e-05,0.00029913]]

#scl = sk.preprocessing.StandardScaler()
#data_scaled = scl.fit_transform(data)
print(data)

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)