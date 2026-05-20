class Geom:
    name = "Geom"


class Line(Geom):  # extended
    def draw(self):
        print("Drawing line")


class Geom:
    name = "Geom"

    def draw(self):
        print("Drawing primitive")


class Line(Geom):
    def draw(self):  # overriding
        print("Drawing line")


class Geom:
    name = "Geom"
    def __init__(self, x0, y1, x2, y2):
        print(f"Initializating Geom for {self.__class__}")
        self.x0 = x0
        self.y0 = y1
        self.x1 = x2
        self.y1 = y2


class Line(Geom):
    def draw(self):
        print("Drawing line")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2,)
        print("Initializing for Rect")
        self.fill = fill

    def draw(self):
        print("Drawing rectangle")


if __name__ == "__main__":
    l = Line(0, 0, 1, 1)
    # print(l.__dict__)
    r = Rect(10, 10, 20, 20, False)
    print(r.__dict__)
