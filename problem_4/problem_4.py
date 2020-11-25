def find_palindrome(n):
    rev = int(''.join(map(lambda x: x ,reversed(list(str(n))))))
    return n == rev

def largest_palindrome_faster():
    max = 999
    largest_palindrome = 0
    while max > 100:
        max2 = max
        if (max * max2 < largest_palindrome):
            break
        while max2 > 100:
            if find_palindrome(max * max2) and (max * max2 > largest_palindrome):
                largest_palindrome = max * max2
            max2 -= 1
        max -= 1
    return largest_palindrome

print(largest_palindrome_faster(), "faster")

def largest_palindrome():
    max = 999
    max2 = 999
    min = 100
    palindromes = []
    while max > min:
        if (max2 < 100):
            max2 = max = max - 1
        if find_palindrome(max * max2):
            palindromes.append(max * max2)
        max2 -= 1
    return list(reversed(sorted(palindromes)))[0]

print(largest_palindrome())
# print(find_palindrome(1234))
# print(find_palindrome(8008))
