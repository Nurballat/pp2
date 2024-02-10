print("Hello World!")

if 5 > 2:
    print("Five is greater than two")
#opazdyvau

#Comments in Python are written with a special character, which one?
#This is a comment

#Use a multiline string to make the a multiline comment:
'''This is a comment
written in 
more than just one line'''

x = 5
x = "Five"
print(x)
print(type(x))

a = 4
A = 'Four'
print(a)
print(A)

x, y, z = '81', '73', '27'
print(x, y, z)

a = b = c = 100
print(a + b + c)

digits = ['one', 'two', 'three']
x, y, z = digits
print(x, y, z)
print(x + y + z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print(len(a))
print('labore' in a)

b = "Hello, World!"
print(b[2:5])

#py strings
#Use the len function to print the length of the string.
x = "Hello World"
print(len(x))

#Get the first character of the string txt.\
txt = "Hello World"
x = txt[0]

#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]

#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

#Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()

#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()

#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace('H', 'J')

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))







