class RedIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Coordinate should be integer!")

    def __set_name__(self, owner, name):
        self.name = "_"+name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = RedIntX()

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z



if __name__ == "__main__":
    pt = Point3D(1,2,3)
    pt.__dict__['xr'] = 5
    print(pt.xr, pt.__dict__, pt.z)

    # h = Integer()
    # print(h.__dict__)