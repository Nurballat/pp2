def un(a):
    uniq = []
    for i in a:
        if a.count(i) == 1:
            uniq.append(i)
    print(uniq)

a = input().split()
for i in range (len(a)):
    a[i] = int(a[i])
un(a)