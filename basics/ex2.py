""" double cycles """

# for i in range(1, 4):
#     for j in range(1, 6):
#         print(f"{i=} {j=}", end=" ")
#     print()


# for i in range(5):
#     print(f"{i=}", end=" ")
#     for j in range(5):
#         print(f"{j=}", end=" ")
#     print()

a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []

for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)

# print(c)

t = ["Tell me   uncle if it was worth it",
     "To study Python   along with this channel",
     "by Sergy    Balakirev",
     "Study is   hard, but reward   is big",
     "So don't be afraid  or   discouraged",
     "Just do your   best   and remember roots"]


for i, line in enumerate(t):
    while line.count("  "):
        line = line.replace("  ", " ")
    t[i] = line

# print(t)

# M, N = list(map(int, input("Enter M and N: ").split()))
M, N = 4, 4

zeros = []

for i in range(M):
    zeros.append([0] * N)

# print(f"{zeros=}")

for i in range(M):
    for j in range(N):
        zeros[i][j] = 1

# print(f"{zeros=}")

A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]

for r in A:
    for x in r:
        print(x, end='\t')
    print()