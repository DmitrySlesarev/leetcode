class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Coord should be integer")


#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, coord):
#         self.verify_coord(coord)
#         self._x = coord
#
#     @property
#     def y(self):
#         return self._y
#
#     @y.setter
#     def y(self, coord):
#         self.verify_coord(coord)
#         self._y = coord
#
#     @property
#     def z(self):
#         return self._z
#
#     @z.setter
#     def z(self, coord):
#         self.verify_coord(coord)
#         self._z = cood


# p = Point3D(1, 2, 3)
# print(p.__dict__)


class DataDescriptor:
    """Data descriptor - has __set__"""

    def __get__(self, obj, objtype=None):
        return "Get from DataDescriptor"

    def __set__(self, obj, value):
        print(f"{self=} {obj=}{value=}")
        print(f"SET in DataDescriptor: {value}")


class NonDataDescriptor:
    """Non-data descriptor - only __get__"""

    def __get__(self, obj, objtype=None):
        print(f"{self=}, {obj=}, {objtype=}")
        return "GET from NonDataDescriptor"


class Example:
    data = DataDescriptor()
    non_data = NonDataDescriptor()


obj = Example()

obj.data = 42  # Goes through DataDescriptor

obj.non_data = 42  # Writes to obj.__dict__['non_data'], bypassing descriptor!
print(obj.non_data)  # Prints: 42 (from instance dict, not descriptor!)

print(Example.non_data)
