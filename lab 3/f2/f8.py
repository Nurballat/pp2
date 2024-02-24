def spy_game(a):
    for i in range(len(a) - 2):
        if(a[i]==0) and (a[i+1]==0) and (a[i+2]==7):
            print("True")
            break
    else:
        print("False")

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
spy_game(a)