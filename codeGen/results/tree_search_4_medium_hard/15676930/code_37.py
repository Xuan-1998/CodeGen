import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(i, n - i) + 1):
        if i == 1:
            dp[i][j] = c[j]
        elif j > 0:
            dp[i][j] = max(dp[i-1][k-1] + b[k-1] for k in range(1, min(j+1, i)))
        else:
            dp[i][j] = a[0]

print(max(dp[-1]))
