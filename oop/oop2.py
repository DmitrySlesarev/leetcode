from icecream import ic

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("__calc__")
        self.__counter += 1
        return self.__counter

c = Counter()
# ic(f"{c.__dict__=}")

# ic(f"{dir(c)}")
# ic(f"{dir(Counter)}")
c()
c2 = Counter()
c2()
c()
c()
c()
print(c.__dict__)
print(c2.__dict__)