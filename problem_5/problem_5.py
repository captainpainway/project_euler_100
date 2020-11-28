from functools import reduce

# Need to get all the primes up to n.
# See problem 3's slow implementation for more info.
def sieve_of_eratosthenes(n):
    arr = list(range(2, n))
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

# This function finds the greatest perfect power of each prime that is <= n.
# Then, it raises each prime to that power and multiplies all the primes together.
def smallest_multiple_factors(n):
    powers = []
    primes = sieve_of_eratosthenes(n)
    for x in primes:
        i = 1
        while x ** i < n:
            i += 1
        powers.append(i - 1)
    return reduce(lambda a, b: a * b, [y ** powers[x] for x, y in enumerate(primes)])

print(smallest_multiple_factors(20))

# Original naive implementation
def smallest_multiple(n):
    largest = n
    all_divisible = False
    while not all_divisible:
        divisors = list(filter(lambda x: largest % x != 0 ,range(1, n + 1)))
        if len(divisors) > 0:
            largest += n
        else:
            all_divisible = True
    return largest

# print(smallest_multiple(20))