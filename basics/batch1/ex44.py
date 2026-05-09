# 5
def make_list():
    """ Make list of numbers which have 3 after division by 5"""
    list_length = input("Enter list lenght:\n>")
    try:
        list_length = int(list_length)
    except ValueError:
        print("Wrong value")
        return
    res = []
    for val in range(int(list_length) + 1):
        if val % 5 != 3:
            continue
        res.append(val)
    return res


# 6
def check_div_by(num: int):
    """ Checks if a value is divided by 3 """
    if not isinstance(num, int):
        raise ValueError("Should be integer!")
    return num % 3 == 0


# 7
def fact(num: int):
    """ Returns factorial of the num """
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Should be integer!")
    if num == 1:
        return num
    return num * fact(num - 1)


# 8
def fibs(num: int):
    """ Returns Fibonacci sum for val """
    if num == 1 or num == 2:
        return num
    res = [1, 1]
    while len(res) < num:
        res.append(res[-2] + res[-1])
        # print(res)
    return sum(res)


# 9
def sec_great_val(collection: [list, tuple]):
    """ Return second great value """
    if type(collection) not in (list, tuple) or len(collection) < 2:
        raise ValueError("Should be tuple or list")
    temp = sorted(collection)
    return temp[-2]


# 10
def ret_odd_sum(num: int):
    """ Return sum of NUM odd values """
    temp = [val for val in range(num + 1) if val % 2 != 0]
    # print(temp)
    return sum(temp)


if __name__ == "__main__":
    # print(make_list())

    # print(check_div_by(randint(1, 100))

    # val = randint(1, 10)
    # print(f"{val=} {fact(val)=}")

    # val = randint(1, 10)
    # print(f"{val=} {fibs(val)=}")

    # print(sec_great_val(list(range(10))))

    print(ret_odd_sum(10))
