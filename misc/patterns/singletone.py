class Singletone:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.__instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.args = args
            self.kwargs = kwargs
