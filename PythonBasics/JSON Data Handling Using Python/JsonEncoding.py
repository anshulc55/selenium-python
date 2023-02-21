import json

# Convert Python dictionary into a JSON formatted String

def send_json_response(argDict):
    print("Convert Python dictionary into a JSON formatted String")
    devString = json.dumps(argDict)
    print(devString)
    return devString

def store_json_response(argDict):
    print("Started writing JSON data into a file")
    with open("sample.json", "w") as file:
        json.dump(argDict, file)

def store_prettyjson_response(argDict):
    print("Started writing Pretty JSON data into a file")
    with open("pretty_sample.json", "w") as file:
        json.dump(argDict, file, indent=4, separators=(", ", ": "), sort_keys=True)

myDict = {
    "name": "Jane Doe",
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}

sampleDict = {
    "colorList": ["Red", "Green", "Blue"],
    "carTuple": ("BMW", "Audi", "range rover"),
    "sampleString": "python.com",
    "sampleInteger": 457,
    "sampleFloat": 225.48,
    "booleantrue": True,
    "booleanfalse": False,
    "nonevalue": None
}

#send_json_response(myDict)
print("*******************")
#send_json_response(sampleDict)
store_json_response(sampleDict)
store_prettyjson_response(sampleDict)