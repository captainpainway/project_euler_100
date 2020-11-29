# Optimized
# The sum of all numbers from 1 to n can be calculated with n(n + 1)/2.
# The sum of all squares is (2n + 1)(n + 1)n/6.
def difference2(n):
    sum = n * (n + 1)/2
    sum_sq = (2 * n + 1) * (n + 1) * n/6
    return sum ** 2 - sum_sq

print(difference2(100))

# Naive implementation, slows down around 10000000.
def sum_of_squares(n):
    return sum([x ** 2 for x in range(1, n + 1)])

def square_of_sums(n):
    return sum(range(1, n + 1)) ** 2

def difference(n):
    return square_of_sums(n) - sum_of_squares(n)

print(difference(100))
