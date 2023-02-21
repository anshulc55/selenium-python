import json

print("Reading JSON Data String")
json_string = '''{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
'''

complex_json = """{
    "id": 23,
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com",
    "experience": {"python":5, "data Science":2},
    "projectinfo": [{"id":100, "name":"Data Mining"}, {"id":200, "name":"Python"}]
}"""

json_complex = json.loads(complex_json)
print(json_complex["name"])
print(json_complex["experience"]["data Science"])
print(json_complex["projectinfo"][1]["id"])

# json_dict = json.loads(json_string)
# print(json_dict)
# print(json_dict["email"])

'''
print("Reading JSON from file")
with open("pretty_sample.json", "r") as jsonfile:
    print("Converting JSON to Python Dictionary")
    json_data = json.load(jsonfile)
    #print(type(json_data))

    for key, value in json_data.items():
        print(key, " : ", value)

    print("Ending File reading")
    print(json_data["sampleString"])
'''


