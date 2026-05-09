N = 7
P = []

for i in range(1, N+1):
    row = [1] * i
    for j in range(i):
        if j == 0:
            continue
        row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)

for r in P:
    print(r)