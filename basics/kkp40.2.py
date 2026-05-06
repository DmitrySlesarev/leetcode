import math


def box_nd(a, b, c, *args, perimeter=True, initial, **kwargs):
    if perimeter:
        return sum((a, b, c, *args)) * 2 ** (len((a, b, c, *args)) - 1) + initial
    else:
        return math.prod((a, b, c, *args)) + initial


if __name__ == "__main__":
    res1 = box_nd(5, 7, 3, initial=0)
    res2 = box_nd(5, 7, 3, 5, 2, initial=0, verbose=True)
    res3 = box_nd(5, 7, 3, 5, 2, initial=-1, perimeter=False)

