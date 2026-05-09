from accessify import private, protected

class Point:
    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    # setter
    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinates should be numbers!")

    # getter
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
# print(pt.x, pt.y)
# pt.x = 200
# pt.y = "coord_Y"
# print(pt.x, pt.y)
# print(pt._x, pt._y)
# print(dir(pt))
# print(pt._Point__x, pt._Point__y)
# print(pt.__x, pt.__y)
# pt.set_coord(100, 200)
# pt.set_coord(100, 'num')
# print(pt.get_coord())
# print("Getters & Setters are interface methods")
# pt.set_coord(100, 200)
# print(pt.get_coord())
# print(pt.__x)
# print(dir(pt))
# print(pt.__dict__)
print(f"{pt._Point__x=}, {pt._Point__y=}")
print(f"{dir(pt)}")
print(f"{pt.check_value(5)}")
