import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys(stdin.readline()).split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (2 ** n) for _ in range(n)]

for i in range(1 << n):
    for j in range(n):
        if ((i >> j) & 1):  # If the j-th hare is fed
            dp[j][i] = max(dp[j][i], dp[(i ^ (1 << j))][j - 1] + a[j])
        else:  # If the j-th hare is not fed
            dp[j][i] = max(dp[j][i], dp[(i ^ (1 << j))][j - 1] + b[j])

max_joy = 0
for i in range(2 ** n):
    max_joy = max(max_joy, dp[n - 1][i] + c[0])

print(max_joy)
