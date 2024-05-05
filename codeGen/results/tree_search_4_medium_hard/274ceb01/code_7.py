from collections import defaultdict

n = int(input())
m = list(map(int, input().split()))

dp = defaultdict(lambda: float('inf'))
dp[0] = 0

for i in range(1, n+1):
    for j in range(m[i-1]+1):
        dp[i].min(j + dp[i-1].get(j, 0), dp[i-1].get(j-1, j) if j > 0 else 0)

print(dp[n])
