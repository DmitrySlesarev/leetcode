""" KKP ex #40.1"""

x, y = (1, 2)

# x, y = (1, 2, 3, 4)  # will not work

x, *y = (1, 2, 3, 4)
# print(x)
# print(y)

*x, y = (1,2,3,4)
# print(x)
# print(y)

x, *y = [1, "a", True, 4]
# print(x)

*x, y, z = "Hello Python"
# print(x)
# print(y)
# print(z)

x = 1, 2, 3
# print(x)

*x, y = 1,2,3
a = [1,2,3]
# print(*a)
b = [4,5,6]
c = [*a, *b]
# print(c)

d = -5, 5
res = range(*d)
# print(res)
# for x in range(*d):
#     print(f"{x=}")
# print(*range(*d))
# for i in [*range(*d)]:
#     print(f"i={i}")

res = [*range(*d), *(True, False), *a]
# print(res)

d = {0: "hopeless", 1: "horrible", 2: "bad", 3: "mediocre", 4: "good", 5: "brilliant"}
# print({*d})
# print({*d.values()})
# print({*d.items()})

d2 = {6: "excellent", 7: "magnificent", 8: "epic"}
# print({**d,**d2})

a, b, *c = d
print(a)
print(b)
print(c)