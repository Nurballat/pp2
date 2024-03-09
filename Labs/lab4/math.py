# ex 1
import math
def Radian(n):
    return math.radians(n)
n = int(input("Input degree: "))
print("Output degree:",Radian(n))

# ex 2
height = int(input())
a = int(input())
b = int(input())
expected_output = (height/2)*(a+b)
print(expected_output)

# ex 3
import math

side = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = (side * length ** 2) / (4 * math.tan(math.pi /side))
print("The area of the polygon is:",math.floor(area))

# ex 4
import math
length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = length * height
print("Expected Output:", area)