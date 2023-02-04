class Record:

    # def __init__(self):
    #     self.name = None
    #     self.age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_values(self):
        print("My Name is - ", self.name, " my Age is - ", self.age)

x = Record("John", 32)
x.city = "Tokyo"
# x.get_values()

print(x.__dict__)
# x.name = "Julia"
# x.get_values()

# y = Record("Peter", 54)
# y.get_values()