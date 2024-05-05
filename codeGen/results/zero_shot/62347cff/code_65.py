import sys
m, n = map(int, input().split())
dp = [[0]*n for _ in range(m)]

for i in range(m):
    dp[i][0] = sum(row[:i+1] for row in zip(*[list(map(int, input().split())) for _ in range(n)]))

for j in range(n):
    dp[0][j] = sum(row[j:j+1] for row in [list(map(int, input().split())) for _ in range(m)])

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + list(map(int, input().split()))[i][j]

print(sum(list(map(int, input().split()))))
