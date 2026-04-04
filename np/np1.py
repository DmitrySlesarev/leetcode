import numpy as np

if __name__ == "__main__":
    a = np.array([1,2,3,4])
    a = np.array([1,2, "3", True])
    print(a)
    print(type(a))
    print(a.dtype)
    print(a[1])
    a[1] = '123'
    print(a[1])
    a[1] = 234
    print(a[1])
    print(a)

    a = np.array([1,2,3,4,5,6,7,8,9])
    print(a)
    print(a[2])
    print(a[ [1,1,1,1,1,1,1] ])
    print(a[ [True, True, False, False, False, False, True, True, True] ])

    b = a.reshape(3,3)
    print(b)
    print(b[1][2])
    print(b[1,2])