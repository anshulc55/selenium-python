class StudentRecord:
    def __init__(self):
        self.name = ""
        self.rollnumber = 0
        self.age = 0


    def inputdata(self):
        self.name = input("Name : ")
        self.rollnumber = input("RollNumber : ")
        self.age = input("Age : ")


    def displaydata(self):
        print("Name - ", self.name)
        print("RollNumber - ", self.rollnumber)
        print("Age - ", self.age)


obj1 = StudentRecord()
obj1.inputdata()

obj2 = StudentRecord()
obj2.inputdata()

obj1.displaydata()
print("****************")
obj2.displaydata()


