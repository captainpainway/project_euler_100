import math

# I looked up the formula for Pythagorean Triples,
# but not the solution to this problem.
# https://www.chilimath.com/lessons/geometry-lessons/generating-pythagorean-triples/
# This is my brute-force solution.
def pythagorean_triplet(s):
    py_sum = 0
    sq = math.floor(math.sqrt(s))
    for m in range(2, sq):
        for n in range(1, sq):
            if (n < m): # m must always be greater than n
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                py_sum = a + b + c
                if py_sum == s:
                    print(a, b, c, py_sum)
                    return a * b * c

print(pythagorean_triplet(1000))