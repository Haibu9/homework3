
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    x = False
    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            x = True
            break

    if x == 0:
        primes.append(i)
    elif i == 2:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)