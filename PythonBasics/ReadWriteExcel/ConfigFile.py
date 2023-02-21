import configparser
import os

file_path = os.getcwd()+"/FileData/sample.ini"

parser = configparser.ConfigParser()
parser.read(file_path)

'''
url = parser.get("bug-details", "url")
username = parser.get("bug-details", "username")
print("Application URL - ", url)
print("Application Username - ", username)
'''

for section in parser.sections():
    print("Section :", section)
    print("Section Keys : ", parser.options(section))
    for key, value in parser.items(section):
        print(key, " = ", value)
    print("")







