""" iter & next functions """

d = [5, 3, 7, 10, 32]

iter(d)

it = iter(d)

next(it)

s = "python"

it2 = iter(s)

next(it2)

r = range(5)

it3 = iter(r)

next(it3)

for x in [1,2,3,4]:
    print(x)


for x in "python":
    print(x)

for x in range(5):
    print(x)

#'for' calls for 'iter'
