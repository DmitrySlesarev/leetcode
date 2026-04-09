# a = [x ** 2 for x in range(1, 5)]
# a = {x:x ** 2 for x in range(1, 5)}
# print(a)

# d = [1, 2, '1', '2', -4, 3, 4]
# # res = set(map(lambda x: int(x), d))
# res = {int(x) for x in d}
# print(res)

# m = {"bad": 2, "normal":3, "good": '4', "perfect": '5'}
# res = {k.capitalize():int(v) for k,v in m.items()}
# print(res)

# d = [1, 2, '1', '2', -4, 3, 4]
# a = {int(x) for x in d if int(x) > 0}
# print(a)

# m = {"hopeless": 0, "pathetic": 1, "unsatisfactory": 2, "satisfactory": 3, "good": 4, "great": 5}
# res = {value:key for key, value in m.items() if 2 <= int(value) <= 5}
# print(res)


def send_mail(from_name, age):
    text = (f"Dear Sergy Balakirev! "
            f"I still didn't get what function was. "
            f"Explain better! I'm only {age}\n"
            f"Best regargs, {from_name}")
    print(text)


send_mail("Dmitry", 40)
send_mail("Dmitry", 40)
