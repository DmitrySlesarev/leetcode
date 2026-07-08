def rect(width, height, /, offset, *, perimeter=True, **kwargs):
    if perimeter:
        return (width * height) * 2 + offset
    else:
        return width * height + offset


res1 = rect(10, 20, 0, )
res2 = rect(10, 20, perimeter=False, offset=5)
res3 = rect(10, 20, 10, perimeter=False)
print(res1)
print(res2)
print(res3)
