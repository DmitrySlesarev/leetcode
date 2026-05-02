class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        return "Drawing smth"


class Line(Geom):
    name = "Line"

    def draw(self):
        return "Drawing line"


class Rect(Geom):
    def draw(self):
        return "Drawing rectangle"


g = Geom()
g.set_coords(3,3, 4,4)
l = Line()
r = Rect()
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)
# print(l.__dict__)
# print(r.__dict__)
print(l.name)
print(r.name)

# print(l.name)
