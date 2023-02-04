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


class StudentResult(StudentRecord):

    def __init__(self):
        self.math = 0
        self.eng = 0
        self.sci = 0
        self.total = 0
        self.per = 0

    def input_data(self):
        self.input_student_data()
        self.eng = int(input('Enter English: '))
        self.math = int(input('Enter Math: '))
        self.sci = int(input('Enter Science: '))
        self.total = self.eng + self.math + self.sci
        self.per = (self.total/300)*100

    def show_student_result(self):
        self.display_record()
        print('English: ', self.eng)
        print('Math: ', self.math)
        print('Science: ', self.sci)
        print('Total Marks: ', self.total)
        print('Percentage: ', self.per)


student = StudentResult()
student.input_data()
student.show_student_result()
