# Method Overiding
class Student:
    def details(self):
        print("My Roll Number is 10. And my name is Jeff")


class Marks(Student):
    def details(self):
        print('English: 82')
        print('Maths: 94')
        print('Computer: 88')

marks = Marks()
marks.details()

stu = Student()
stu.details()
# # Method Overloading
# class Shape:
#     def area(self, x=None, y=None):
#
#         if x!=None and y==None:
#             print("Area of Square is - ", x*x)
#
#         if x!=None and y!=None:
#             print("Area of a rectangle is - ", x*y)
#
# shape = Shape()
# shape.area(5)
# shape.area(10, 5)