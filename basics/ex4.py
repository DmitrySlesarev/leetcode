t = ["+7", "+6", "+5", "+4"]
# print(dict.fromkeys(t, 'country code'))

# d = {1:True, 0:False}
# print(d)
# print(d.clear())
# print(d)

d = {True: 1, False: 'False', 'list': [1,2,3], 5:5}
# print(d)
# d2 = d.copy()
# print(d2)
# d3 = dict(d)
# print(d3)
# print(f"{id(d)=}, {id(d2)=}, {id(d3)=}")

# print(d.get("list"))
# print(d["list"])
# # print(d[3])
# print(d.get(3))
# print(d.get(3, False))

# print(d.setdefault('list'))
# print(d)
# print(d.setdefault('unknown'))
# print(d)
# print(d.setdefault('unknown'))
# print(d)
# del d['unknown']
# print(f"{d=}")

print(d)
# d.pop(True)
# print(d)
# print(d.pop(True, False))

# d.popitem()
# print(d)
# d.popitem()
# print(d)
# # {}.popitem()
# print(d.keys())
# for x in d:
#     print(x)
# print(d.values())
# for _ in d.values():
#     print(_)
# for x in d.items():
#     print(x)
# print(d.items())
# for k,v in d.items():
#     print(k,v)

d = dict(one = 1, two = 2, three = '3', four = '4')
d2 = {2: 'bad', 3: 'normal', 'four': 'good', 'five': 'excellent'}
# d.update(d2)
# # print(d)
print(d)
# print(d | d2)
# print(d2 | d)
d3 = {**d, **d2}
print(d3)
