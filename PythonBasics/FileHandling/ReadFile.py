import os

def read_file(filename):
    #fb = open(os.getcwd() + "/Files/" + filename, 'r')
    try:
        with open(os.getcwd() + "/Files/" + filename, 'r+') as file:
            print(file.read())
    except Exception as e:
        print(e)


def read_n_lines(filename, number_of_lines):
    try:
        with open(os.getcwd() + "/Files/" + filename, 'r+') as file:
            for line in range(number_of_lines):
                print(file.readline().strip())
    except Exception as e:
        print(e)


#read_file("TESTFILE.txt")
read_n_lines("TESTFILE.txt", 4)

# read()
# readline()
# readlines()