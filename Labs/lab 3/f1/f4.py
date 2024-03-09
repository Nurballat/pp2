'''a = []
n = int(input("quanity of elements:"))
for i in range(n):
    a.append(int(input()))
print(a)'''

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

for i in range(len(a)):
    for j in range(2, a[i]):
        if(a[i] % j == 0):
            break
    else:
        print(a[i])
