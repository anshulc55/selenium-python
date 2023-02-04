# Retrun Cube of a Value

# def cube(a):
#     n = a*a*a
#     return n
#
#
# x = int(input("Enter the Value : "))
# print(f"Cube of Given Value is ", cube(x))

def calcuteOperations(a, b):
    add = a + b
    mul = a * b
    div = a / b
    sub = a - b
    return add, mul, div, sub

a, b, c, d = calcuteOperations(10, 2)
print(f"Addition - ", a)
print(f"Multiplication - ", b)
print(f"Divison - ", c)
print(f"Substraction - ", d)