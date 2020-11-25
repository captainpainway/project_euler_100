# Naive implementation
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

print(smallest_multiple(20))