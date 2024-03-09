class string():
    def __init__(self):
        self.input_str = ""

    def getString(self):
        self.input_str = input("Input:")

    def printString(self):
        print(self.input_str.upper())

s = string()
s.getString()
s.printString()


