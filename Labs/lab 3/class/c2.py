'''Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Определите класс с именем Shapeи его подкласс Square. В Squareклассе есть init функция, которая принимает в length качестве аргумента.
 Оба класса имеют areaфункцию, которая может печатать область фигуры, где площадь фигуры по умолчанию равна 0.
'''

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0;
class Square(Shape):
    def __init__(self, l):
        super().__init__()
        self.l = l

    def area(self):
        return(self.l ** 2)

shape = Shape()
print("Area of shape: ", shape.area())

l = int(input("Square length: "))
square = Square(l)
print("Area os square: ", square.area())