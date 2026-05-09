class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # # old = 4
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person("Sergey", 20)
del p.old
# p.set_old(35)
# print(p.get_old())
# p.__dict__['old'] = 'old'
# p.old = 35
# print(p.old, p.__dict__)
print(p.__dict__)
