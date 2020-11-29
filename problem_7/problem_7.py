import itertools

# This takes a few seconds, but works.
def count_sieve(idx):
    primes = [2]
    i = 1
    for x in itertools.count(start = 3, step = 2):
        prime = True
        for j in primes:
            if x % j == 0:
                prime = False
        if prime == True:
            primes.append(x)
            i += 1
        if i == idx:
            break
    return primes[i - 1]

print(count_sieve(10001))

# This isn't going to be good enough to get 100001 primes.
def modified_sieve(n):
    primes = [2]
    for x in range(3, n, 2):
        prime = True
        for j in primes:
            if x % j == 0:
                prime = False
        if prime == True:
            primes.append(x)
    return primes

# print(modified_sieve(100000))
