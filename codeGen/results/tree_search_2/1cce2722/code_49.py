import sys

n = int(input())
a = list(map(int, input().split()))

dp = {0: n}

for i in range(n):
    if a[i] == a[0] + 1 or a[i] == a[0] - 1:
        dp[i] = min(dp.get(max(0, i-2), 0), dp.get(min(n-1, i+2), n)) + 1
    else:
        dp[i] = n

print(min(dp.values()))
