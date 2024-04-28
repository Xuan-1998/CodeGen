n, m = map(int, input().split())
res = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if i < j:
            res[i][j] = min(res[i-1][j], res[i][j-1]) + 1
        elif i == j:
            res[i][j] = 1
print(res[-1][-1])
