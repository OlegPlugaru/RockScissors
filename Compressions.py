# List Compression
numbers = [1, 2, 3, 4, 5]
# Var1
# numbers_pow_2 = []
# for n in numbers:
#     numbers_pow_2.append(n**2)
# Var 2
#numbers_pow_2 = list(map(lambda n : n**2, numbers))
# Var 3   
numbers_pow_2 = [n**2 for n in numbers]
print(numbers_pow_2)