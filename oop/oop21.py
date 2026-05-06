class Geom:
    pass


class Line(Geom):
    pass


class Vector(list):
    # def __str__(self):
    #     return " ".join(map(str, self))
    pass


if __name__ == "__main__":
    # print(Geom.__name__)
    g = Geom()
    # print(g)
    l = Line()
    print(l.__class__)
    # print(issubclass(Line, Geom))
    # print(issubclass(Geom, Line))
    # print(issubclass(l, Geom))  # raises
    # print(isinstance(l, Geom))  # True
    # print(isinstance(l, object))  # True
    # print(isinstance(Geom, object))  # True
    # print(issubclass(int, object))
    # print(issubclass(list, object))

    v = Vector([1, 2, 3])
    print(v)
    print(type(v))
