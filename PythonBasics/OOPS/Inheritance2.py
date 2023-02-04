class StudentRecord:

    def __init__(self):
        self.name = ""
        self.rollnumber = 0

    def input_student_data(self):
        self.name = input("Name : ")
        self.rollnumber = int(input("RollNumber : "))

    def display_record(self):
        print("Student Name : ", self.name)
        print("Student RollNumber : ", self.rollnumber)


class StudentDetails(StudentRecord):

    def __init__(self):
        #StudentRecord.__init__(self)
        super().__init__()
        self.classname = ""
        self.section =""

    def input_data(self):
        super().input_student_data()
        self.classname = input("Class Name : ")
        self.section = input("Section : ")

    def display_all_details(self):
        super().display_record()
        print("ClassName is : ", self.classname)
        print("Section is : ", self.section)


studentdata = StudentDetails()
studentdata.input_data()
studentdata.display_all_details()