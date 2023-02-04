import os
import datetime


def create_file(filename):
    fb = open(os.getcwd() + "/Files/" + filename, 'w')
    fb.write("Hi, I am Sample 3 file")
    fb.close()


def is_file_present(filename):
    # print(os.listdir())
    print(os.path.isfile(os.getcwd() + "/Files/" + filename))


timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%d-%m-%Y-%H-%M-%S.txt")

print(os.getcwd())
create_file(timestamp)
is_file_present(timestamp)
