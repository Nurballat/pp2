class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        super().__init__()
        self.l = l

    def area(self):
        return self.l ** 2

# Create an instance of Shape
shape = Shape()
print("Area of shape:", shape.area())

# Create an instance of Square
side_length = int(input("Enter the side length of the square: "))
square = Square(side_length)
print("Area of square:", square.area())
