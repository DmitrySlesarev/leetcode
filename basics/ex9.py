class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.att1 = None


if __name__ == "__main__":
    obj1 = Singleton()
    obj1.att1 = 20

    obj2 = Singleton()
    print(obj2.att1)  # Will print 20 since obj2 is the same instance as obj1