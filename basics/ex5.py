from pympler import asizeof

a = (1,2,3)

print(type(a))
print(asizeof.asizeof(a))

a = [1,2,3]
print(type(a))
print(asizeof.asizeof(a))