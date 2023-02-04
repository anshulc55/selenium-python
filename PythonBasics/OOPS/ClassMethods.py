class StudentRecord:

    name = "Maria"
    age = 20

    @classmethod
    def updatedata(self):
        self.name = "Peter"
        self.age = 24


obj1 = StudentRecord()
obj2 = StudentRecord()

print("Before Update the Class Varaibles")
print("Name : ", obj1.name)
print("Age : ", obj1.age)
print("Name : ", obj2.name)
print("Age : ", obj2.age)

StudentRecord.updatedata()

print("After Update the Class Varaibles")
print("Name : ", obj1.name)
print("Age : ", obj1.age)
print("Name : ", obj2.name)
print("Age : ", obj2.age)