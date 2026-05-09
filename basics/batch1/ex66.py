from icecream import ic

a = [1 for x in range(5)]
print(a)
N = 7
a = [1 for x in range(N)]
# print(a)
# print(x)
# for x in range(10):
#     print(x)
# print(x, 2)
ic([1] * N)
a = [x % 4 for x in range(N)]
ic(a)
a = [x % 2 == 0 for x in range(N)]
ic(a)
a = [0.5 * x + 1 for x in range(N)]
ic(a)

# d_inp = input("Integers separated by space: ")

# a = [int(d) for d in d_inp.split()]
# ic(a)
# a = list(map(int, d_inp.split()))
# ic(a)
a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
c = list(zip(a, b))
# ic(c)

a = [d for d in 'python']
# ic(a)
a = [ord(d) for d in 'python']
# ic(a)

a = [x for x in range(-5, 5) if x < 0]
# ic(a)
a = [x for x in range(-5, 5) if x % 2 == 0]
# ic(a)
a = [x for x in range(-6, 7) if x % 2 == 0 and x % 3 == 0]
# ic(a)
cities = ["New York City", "Miami", "St Louis", "Nashville", "San Francisco"]
a = [city for city in cities if len(city) < 7]
# ic(a)

d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
r = [
    'odd' if num % 2 else 'even'
    for num in d
    if num > 0
]
ic(r)
