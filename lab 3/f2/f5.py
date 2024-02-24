'''?'''

s = input("Enter a sentence: ")
a = s.split(" ")
print("Original list:", a)
print(len(a))
for i in range(len(a)):
    a[i] = a[len(a) - i - 1]

print("Reversed list:", a)
#bir eki ysh tort bes alty