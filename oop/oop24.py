from abc import abstractmethod, ABC


class Geom(ABC):
    @abstractmethod
    def get_pr(self):
        raise NotImplemented("'get_pr' should be implemented")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


if __name__ == "__main__":
    r1 = Rectangle(1, 2)
    r2 = Rectangle(3, 4)
    s1 = Square(10)
    s2 = Square(20)

    geom = [r1, r2, s1, s2]
    for g in geom:
        print(g.get_pr())
    # print(r1.get_rect_pr(), r2.get_rect_pr())
    # print(s1.get_sq_pr(), s2.get_sq_pr())
