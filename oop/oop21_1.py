# class Geom(object):
class Geom:  # from Python3.x
    pass

class Line(Geom):
    pass

class Vector(list):
    # pass
    def __str__(self):
        return " ".join(map(str, self))


if __name__ == "__main__":
    # print(Geom.__name__)
    g = Geom()
    l = Line()
    # print(g)
    # print(l.__class__)
    # print(issubclass(Line, Geom))
    # print(issubclass(Geom, Line))
    # # print(issubclass(l, Line))  # error
    # print(isinstance(Line, Geom))
    # print(isinstance(Geom, Line))
    # print(isinstance(g, Line))
    # print(isinstance(l, Line))
    # print(issubclass(int, object))
    # print(issubclass(list, object))
    v = Vector([1,2,3])
    print(v)