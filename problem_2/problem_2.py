def fib(n):
    a = 1
    b = 2
    acc = [2]
    while b < n:
        c = a + b
        a = b
        b = c
        if c % 2 == 0 and c < n:
            acc.append(c)
    return sum(acc)

print(fib(4000000))