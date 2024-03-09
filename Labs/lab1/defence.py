n = int(input())
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
         print(i)

'''n = int(input("Рост:"))
if (n < 175):
    print("Pg")
elif (n >= 175) and (n <= 190):
    print("Choose sg or sf" )
else:
    print("Hola Shaq!")

def sum(a,b):
    print(a+b)

x = int(input())
y = int(input())
sum(x,y)
 '''
