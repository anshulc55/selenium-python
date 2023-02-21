import json
def validateJSON(jsonString):
    try:
        json.loads(jsonString)
    except Exception as e:
        print(e)
        return False
    return True


jsonData = '''{
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

isValidJSON = validateJSON(jsonData)
print("Is Given JSON Valid : ", isValidJSON)
