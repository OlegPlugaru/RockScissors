# map(), filter(), reduce()
from functools import reduce

numbers = [1, 2, 3]

# def double(a):
#     return a * 2



result = map(lambda a : a * 2, numbers)

print(list(result))


# def isEven(n):
#     return n % 2 == 0

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

# sum = 0
# for expense in expenses:
#     sum += expense[1]

sum = reduce(lambda a,b : a[1] + b[1], expenses)

print(sum)