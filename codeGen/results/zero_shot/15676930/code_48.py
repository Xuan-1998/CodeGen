import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = a[i - 1]
    dp[0][i] = 0

for length in range(2, n + 1):
    for left in range(n - length + 1):
        right = left + length
        if length % 2 == 1:
            dp[left][right] = max(b[left], b[right])
        else:
            dp[left][right] = min(a[left], a[right])

max_joy = 0

for i in range(1, n):
    max_joy += dp[0][i]

print(max_joy)
