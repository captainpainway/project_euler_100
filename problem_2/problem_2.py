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

def fib2(n):
    arr = [1, 2]
    while True:
        if arr[-1] + arr[-2] > n:
            break
        arr.append(arr[-1] + arr[-2])
    return sum(filter(lambda x: x % 2 == 0 ,arr))

print(fib2(4000000))

# Only adding every third number, which is even
def fib3(n):
    acc = 0
    a = 1
    b = 1
    while True:
        c = a + b
        if c > n:
            break
        acc += c
        a = c + b
        b = a + c
    return acc

print(fib3(4000000))