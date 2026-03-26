class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y


if __name__ == "__main__":
    p = Point(1, 1)
    # print(len(p))
    # print(bool(p))
    if p:
        print("Object p returns True")
    else:
        print("Object p returns False")
