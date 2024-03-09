def histogram(a):
    for i in range(len(a)):
        print("*" * a[i])

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

histogram(a)

