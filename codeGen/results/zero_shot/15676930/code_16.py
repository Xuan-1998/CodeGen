import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = a[i]
    elif i == 1:
        dp[i] = max(a[i], b[i-1])
    else:
        dp[i] = max(dp[i-2] + c[i], dp[i-1] + b[i-1])

print(max(dp))
