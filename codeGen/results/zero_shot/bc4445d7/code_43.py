n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
m = int(input())
p = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i][i] = 1

for length in range(3, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = max(dp[i][j], dp[i][k] + p[0] * (dp[k + 1][j] if j > k else 0))

print(dp[1][n] % (10 ** 9 + 7))
