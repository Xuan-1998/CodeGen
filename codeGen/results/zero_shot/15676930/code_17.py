import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1]) if i % 3 == 1 else \
            max(dp[i - 1], dp[i - 2] + b[i - 1]) if i % 3 == 2 else \
            dp[i - 1] + c[i - 1]

print(dp[n])
