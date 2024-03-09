def has(a):
    for i in range(len(a) - 1):
        if (a[i] == 3) and (a[i+1] == 3):
            print("True")
            break
    else:
        print("False")

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
has(a)

