# Hierarchical Inheritance
class A:
    def displaySelf(self):
        print("I am Class A")

    def firstClass(self):
        print("Hi, I am from Class A")


class B(A):
    def displaySelf(self):
        super().displaySelf()
        print("I am Class B")


class C(A):
    def displaySelf(self):
        super().displaySelf()
        super().firstClass()
        print("I am Class C")

b = B()
c = C()

b.displaySelf()
c.displaySelf()

# # MultiLevel Inheritance
# class A:
#     def displaySelf(self):
#         print("I am Class A")
#
#     def firstClass(self):
#         print("Hi, I am from Class A")
#
#
# class B(A):
#     def displaySelf(self):
#         super().displaySelf()
#         print("I am Class B")
#
#
# class C(B):
#     def displaySelf(self):
#         super().displaySelf()
#         super().firstClass()
#         print("I am Class C")
#
# c = C()
# c.displaySelf()

# #Multiple Inheritance
# class A:
#     def displaySelf(self):
#         print("I am Class A")
#
#
# class B:
#     def displaySelf(self):
#         print("I am Class B")
#
#     def secondMethod(self):
#         print("Hi, I am Second Method of Class B")
#
#
# class C(A, B):
#     def displaySelf(self):
#         A.displaySelf(self)
#         B.displaySelf(self)
#         super().secondMethod()
#         print("I am Class C")
#
# c = C()
# c.displaySelf()




#Single Inheritance
# class A:
#     def displaySelf(self):
#         print("I am Class A")
#
#
# class B(A):
#     def displaySelf(self):
#         super().displaySelf()
#         print("I am Class B")
#
# b = B()
# b.displaySelf()