def is_Prime(n):
    if n < 2:
        return False

    else:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

prime_numbers = list(filter(lambda x: is_Prime(x), a))

print(prime_numbers)