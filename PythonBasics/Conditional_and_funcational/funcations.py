# Functions in Python
def simpleInterest(p, r, t):
    si = (p*r*t)/100
    print(f"Simple Interest is - ", si)


prinicipal = int(input("Enter Prinicipal Amount : "))
rate = int(input("Enter rate of Interest : "))
time = int(input("Enter time in years : "))
simpleInterest(prinicipal, rate, time)


# def message():
#     print("Hello, I am Function")
#
#
# def addition(a, b):
#     c = a + b
#     print(f"Addition of a and b is - ", c)
#
#
# message()
# addition(10, 12)
# addition(50, 8)