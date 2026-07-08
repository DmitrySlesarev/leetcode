def triangle(a, b, c=4, /):
    return a + b + c


res1 = triangle(10, 20, 30)
res2_5 = triangle(10, 20)
# res2 = triangle(10, c=20, b=30)

print(res2_5)


def triangle(a, b, c, /, mul, offset=0):
    return (a + b + c) * mul + offset


res1 = triangle(10, 20, 30, mul=1)
res2 = triangle(10, 20, 30, offset=10, mul=2)

print(res2)


def polyline(a, b, /, *args, mul=1, offset=0, **kwargs):
    return (a + b + sum(args)) * mul + offset


res1 = polyline(0, 5, mul=2)

print(res1)
