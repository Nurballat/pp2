def polindrome(s):
    if (len(s)>2):
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                print("Not polindrome")
                break
        else:
            print("Polindrome")
    else:
        print("Not polindrome")

s = input()
polindrome(s)