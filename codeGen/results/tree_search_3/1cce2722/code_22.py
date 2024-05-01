from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dp = [defaultdict(int) for _ in range(n + 1)]

for i in range(2, n + 1):
    for k in range(1, i):
        if a[i - 1] == a[k]:
            dp[i][k] = max(dp[i - 1][j] - 1 for j in range(k + 1)) if i > 0 else 0
        else:
            dp[i][k] = dp[i - 1][k]

print(max(dp[-1].values()))
