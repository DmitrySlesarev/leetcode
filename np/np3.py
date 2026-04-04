import numpy as np

if __name__ == "__main__":
    print(np.array([0] * 10))
    print(np.array([1] * 15))
    print(np.array( [ x for x in range(10) ] ))
    print(np.empty(10))
    print(np.empty(10, dtype='int16'))
    print(np.empty((3,2), dtype='int16'), sep=" ")
    print(np.empty((3,2), dtype='int16'))
    print(np.eye(4))
    print(np.eye(4,2))
    print(np.identity(5))