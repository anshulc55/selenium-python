class BasicMath:

    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def substract(x, y):
        return x - y

    @staticmethod
    def divide(x, y):
        return x/y


print("Enter the Value of X and Y")
x = int(input("x : "))
y = int(input("y : "))

print("Addition is : ", BasicMath.add(x, y))
print("Substraction is : ", BasicMath.substract(x, y))
print("Multiplication is : ", BasicMath.multiply(x, y))
print("Devision is : ", BasicMath.divide(x, y))