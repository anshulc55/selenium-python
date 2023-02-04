class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    #getter
    def get_age(self):
        return self.__age

    #Setter
    def set_age(self, age):
        if age <=3:
            print("Age is not Valid, Student must be older than 3 years")
        elif age >= 30:
            print("Age is not valid, Student must be uder 30")
        else:
            self.__age = age


stu = Student("Peter", 14)
print("Name is :", stu.name, " and Age is -", stu.get_age())

stu.set_age(2)
print("Name is :", stu.name, " and Age is -", stu.get_age())