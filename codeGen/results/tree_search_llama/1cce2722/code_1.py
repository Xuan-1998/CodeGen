import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

def f(i, j):
    if a[i] != a[j] + 1 and a[i] != a[j] - 1:
        return 1
    elif a[i] == a[j] + 1:
        return sum(1 for k in range(j+1, i) if a[k] == a[j] + 2)
    else:
        return sum(1 for k in range(j-1, i) if a[k] == a[j] - 2)

for i in range(1, n + 1):
    for j in range(i - 1):
        dp[i][j] = max(dp[i-1][k] + f(i, j) for k in range(j-1, j+2))

print(max(0, dp[n][0]))
