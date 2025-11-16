#deserializer is not working................////////////
import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"
data={
    'teacher_name':'Jim',
    'course_name':'Matching Learning',
    'course_time':3,
    'seat':'20'
}

#python data convart to json data(dumps) etai mainli json e convert korar jonno use kora hoyese
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data1 = r.json()
print(data1)