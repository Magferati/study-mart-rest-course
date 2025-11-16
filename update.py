import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"
data={
    'id':2,
    'teacher_name':'Jim',
    'course_name':'Matching Learning'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data1 = r.json()
print(data1)