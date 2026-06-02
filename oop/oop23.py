class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"init of Geom for {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

    def get_coords(self):
        return (self._x1, self._y1)


if __name__ == "__main__":
    r = Rect(0, 0, 10, 20)
    r.get_coords()
    print(r.__dict__)
    print(r._x1, r._y1, r._x2, r._y2)

    print(r.name)
