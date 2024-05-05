import sys

n = int(input())
m = list(map(int, input().split()))
dp = [0] * (n + 1)
next = [0] * (n + 1)

for i in range(n):
    for j in range(i):
        if m[j] > m[i]:
            dp[i + 1] = (dp[i + 1] + dp[j]) % (10**9 + 7)

print(dp[-1])
