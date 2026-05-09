# a  = [(i,j)
#       for i in range(3) if i % 3 == 0
#       for j in range(4) if j % 2 == 0
#       ]
# print(a)

# a = [ f"{i}*{j}={i*j}"
#       for i in range(1, 10)
#       for j in range(1, 10)
#       ]
# print(*a, sep="\n")

# matrix = [[0, 1, 2, 3],
#           [10, 11, 12, 13],
#           [20, 21, 22, 23]
#           ]
#
# a = [x
#      for row in matrix
#      for x in row
#      ]
# print(a)
#
#
def cust_timer(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter
        start = perf_counter()
        ret = func(*args, **kwargs)
        stop = perf_counter()
        print(f"Elapsed time {stop - start}")
        return stop - start

    return wrapper
#
#
# @cust_timer
# def t1():
#     a = [(i, j) for i in range(10) for j in range(10)]
#     return a
#
#
# @cust_timer
# def t2():
#     res = []
#     for i in range(10):
#         for j in range(10):
#             res.append((i, j))
#     return res
#
# print(f"{t1()} & {t2()} {t2()/t1() * 100:.6f}%")
# print()

# M, N = 3, 4
#
# matrix = [[a for a in range(M)] for b in range(N)]
#
# print(matrix)

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for col, lst in enumerate(A):
#     for row, val in enumerate(lst):
#         A[col][row] = val ** 2
# print(A)
#
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [[val**2 for row, val in enumerate(lst)] for col, lst in enumerate(A)]
# print(res)

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [[val ** 2 for val in col] for col in A]
# opt = [x **2
#        for row in A
#        for x in row
#        ]
# print(A, res, sep="\n")
# print(opt)
res = [[row[i] for row in A] for i in range(len(A[0]))]
print(res)