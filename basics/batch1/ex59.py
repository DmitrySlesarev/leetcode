from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшюъьыюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, name, age, ps, weight):
        self.verify_name(name)
        
        self.__name = name
        self.age = age
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_name(cls, fio):
        if type(fio) != str:
            raise TypeError("Name should be string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Wrong name format")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("Name should contain at least 1 symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError("You're allowed to use letters and dash only")

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError("Age should be a number of range [14; 120]")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Weight should be a real number from 20 and higher")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Should be string!")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Wrong passport format")

        for p in s:
            if not p.isdigit():
                raise TypeError("Should be digits")

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        self.verify_age(val)
        self.__age = val

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, val):
        self.verify_ps(val)
        self.__ps = val

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        self.verify_weight(val)
        self.__weight = val


p = Person('Donald Trump Junior', 60, '1234 567890', 80.0)
p.age = 90
p.ps = "4567 123456"
p.weight = 70.0
print(p.__dict__)
print(p.age)
# p.weight = 12

