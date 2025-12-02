import requests
import json
URL = 'http://127.0.0.1:8000/aicreate/'

data = {
    'id': 4,
}
json_data = json.dumps(data) #dumps methode python data ke json e convart kore
r = requests.delete(url=URL, data=json_data)
data = r.json()
print(data)