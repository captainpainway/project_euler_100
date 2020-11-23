import math

def faster_prime_factor(n):
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n = n / factor
        else:
            factor += 1
    return last_factor

print(faster_prime_factor(13195))
print(faster_prime_factor(600851475143))

def prime_factor(n):
    s = math.ceil(math.sqrt(n) / 2)
    primes = sieve_of_eratosthenes(s)
    for p in reversed(primes):
        if n % p == 0:
            return p

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
def sieve_of_eratosthenes(s):
    arr = list(range(2, s))
    next_prime = 0
    while next_prime < len(arr) / 2:
        for x in arr:
            if x != None and x > next_prime:
                next_prime = x
                break
        prime_idx = arr.index(next_prime)
        for i in range(prime_idx + next_prime, len(arr), next_prime):
            arr[i] = None
    return [a for a in arr if a]

#print(prime_factor(13195))
#print(prime_factor(600851475143))

# Getting a recursion depth error
def sieve_recursive(s):
    arr = list(range(2, s))
    next_prime = 0
    def iterate(arr, next_prime):
        for x in arr:
            if x != None and x > next_prime:
                next_prime = x
                break
        prime_idx = arr.index(next_prime)
        for i in range(prime_idx + next_prime, len(arr), next_prime):
            arr[i] = None
        if next_prime >= len(arr) / 2:
            return arr
        else:
            iterate(arr, next_prime)
    iterate(arr, next_prime)
    return [a for a in arr if a]
