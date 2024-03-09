import random
x = random.randrange(1, 21)
name = input("Hello! What is your name? ")
print("Well, " + name + " I am thinking of a number between date.py and 20.")
y = 0
trys = 1
while(True):
    y = int(input("Take a guess:"))
    if y == x:
        print("Good job," + name + "! You guessed my number in " + str(trys) + " guesses!")
    elif y > x:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    trys+=1


