===BEGIN CODE===
n = int(input())
p = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    if p[i - 1] > i:
        dp[i][i] = 2
    else:
        dp[i][p[i - 1]] = (dp[p[i - 1]][i - 1] + 1) % 1000000007

res = 0
for i in range(1, n + 1):
    res += dp[i][n]

print(res)
