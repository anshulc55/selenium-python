import os
import datetime

def write_file(filename):
    try:
        with open(os.getcwd() + "/Files/" + filename, 'a') as file:
            text = "Hi, This is a Modification."
            text1 = "Writing from Writelines Method"
            text2 = ['\nName: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
            file.write("\n")
            file.write("              ")
            file.write(text)
            file.write("\n")
            file.writelines(text1)
            file.writelines(text2)

    except Exception as e:
        print(e)

# writelines()
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%d-%m-%Y-%H-%M-%S.txt")
print("File Name is - ", timestamp)
write_file("test1.txt")