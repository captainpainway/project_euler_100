def multiples(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples(1000))

def mult(n):
    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(n))))

print(mult(1000))