class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle():
    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w

    def area(self):
        return(self.w * self.l)

l = int(input("Length: "))
w = int(input("Width: "))

rect = Rectangle(l, w)
print("Area of Rectangle: ", rect.area())

