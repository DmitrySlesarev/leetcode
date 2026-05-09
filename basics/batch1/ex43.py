# n = int(input("> "))
#
# if n < 1 or n > 100:
#     print("Wrong number")
# else:
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#
#     print(f"Factorial {n}! = {p}")

# for i in range(1, 7):
#     print('*' * i)

words = ["God", "give", "me", "power", "to", "finish", "this", "course"]

# s = ''
# flag_first = True
# for w in words:
#     s += ('' if flag_first else ' ') + w
#     flag_first = False
#
# print(s)

# s = ''
# for w in words:
#     s += ' ' + w
#
# print(s.lstrip())

# print(" ".join(words))

digs = [4, 3, 100, -53, -30, 1, 34, -8]

# for x in range(len(digs)):
#     if 10 <= abs(digs[x]) <= 99:
#         digs[x] = 0
#
# print(digs)

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0

print(digs)