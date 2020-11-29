import itertools

# This takes a few seconds, but works.
# Start with two already in the primes list.
# As we count up by twos from three (twos can't be prime),
# see if the number is divisible by any previous prime.
# If not divisible, it is prime, and add it to the list of primes.
# Also increment the index so we can return just the 10,001st prime (at index 10000).
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
