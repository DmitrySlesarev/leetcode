class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Wrong index!")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index should be integer & non-negative value")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index should be integer & non-negative value")

        del self.marks[key]

if __name__ == "__main__":
    s1 = Student("Sergy", [5, 5, 3, 2, 5])
    # print(s1.marks[2])
    # print(s1[2])
    s1[10] = 4
    print(s1[2])
    print(s1.marks)

    del s1[2]
    print(s1.marks)
