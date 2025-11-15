""" Use of 'property' """
from string import ascii_letters


class Person:
    def __init__(self, name, age, ps, weight):
        self.verify_name(name)

        self.__name = name.split()
        self.__age = age
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_name(cls, name):
        if type(name) != str:
            raise TypeError("Should be string")

        f = name.split()
        if len(f) != 3:
            raise TypeError("Wrong name format")

        letters = ascii_letters
        for s in f:
            if len(s) < 1:
                raise TypeError("At least 1 symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError("Only latin characters")
