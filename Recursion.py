# Recursion

# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(7))


def minus(n):
    if n == 1: return 1
    print(n)
    return n * minus(n-1)

print(minus(4))


