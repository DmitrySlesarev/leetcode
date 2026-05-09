# print(dict.fromkeys([0]))

t = ["+7", "+6", "+5", "+4", "+3"]
#
# d = dict.fromkeys(t)
# print(d, type(d))

d = dict.fromkeys(t, "country code")
print(d)

d.clear()
print(d)

d = {True: 1, False: "False", "list": [1,2,3], 5:5}
print(d)

d2 = d
print(id(d2) == id(d))
print(d2 is d)

d2 = d.copy()
print(id(d2) == id(d))
print(d2 is d)

d2 = dict(d)
print(id(d2) == id(d))
print(d2 is d)

print(d.get("list"))
print(d.get("unknown"))

print(d.get("new", False))

print(d.setdefault("3"))
print(d)
print(d.setdefault("3"))
print(d)

del d["3"]
print(d)

print(d.setdefault("3", "three"))
print(d)

d.pop("3")
print(d)
print(d.pop("abc", False))

d.popitem()
print(d)

print(d.keys())
d = {True: 1, False: "False", "list": [1,2,3], 5:5}
print(d.keys())

for x in d:
    print(x)

print(d.values())

for x in d.values():
    print(x)

for k,v in d.items():
    print(k,v)

print(d.items())
print(d.values())

x, y = (1,3)
print(x, y)

for key, value in d.items():
    print(key, value)

d = dict(one =1, two=2, three="3", four="4")
d2 = {2: "bad", 3: "normal", "four":"good", 5: "excellent"}
print(d, d2)
# print(d.update(d2))
# print(d)
print(d | d2)
print(d, d2)
d3 = {**d, **d2}
print(d3)
d4 = {**d2, **d}
print(d4)