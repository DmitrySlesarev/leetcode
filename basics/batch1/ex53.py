# n = int(input("Enter integer less than 100: "))
#
# if n < 1 or n > 100:
#     print("Wrong integer")
# else:
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#
#     print(f"Factorial {n}! = {p}")

# for i in range(1, 7):
#     print("*" * i)

words = ["God", "give", "me", "power", "to", "get", "through", "this"]

# s = ''
# flag = True
# for w in words:
#     s += ("" if flag else " ") + w
#     flag = False
#
# print(s)
# print(s.lstrip())

# s = ''
# for w in words:
#     s += ' ' + w
#
# print(s.lstrip())

# s = " ".join(words)
# print(s)

digits = [4, 3, 10, -53, -30, 1, 34, -8]
# for i in range(len(digits)):
#     if 9 < abs(digits[i]) < 100:
#         digits[i] = 0
#
# print(digits)

# for i, val in enumerate(digits):
#     if 9 < abs(val) < 100:
#         digits[i] = 0
# print(digits)

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
     'shch', '', 'y', '', 'e', 'yu', 'ya'
]

start_index = ord('а')
title = "Программирование на Python - лучший курс"
slug = ''

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s in " !?;:.,":
        slug += '-'
    else:
        slug += s

while slug.count('--'):
    slug = slug.replace('--', '-')

print(slug)