class Record:
    data = "John"

    def getValue(self):
        print("Data Value is ", self.data)

    def updateData(self):
        self.data = "Maria"

abc = Record()
xyz = Record()

abc.getValue()
xyz.getValue()
print("********************")

xyz.data = "Peter"
abc.getValue()
xyz.getValue()
