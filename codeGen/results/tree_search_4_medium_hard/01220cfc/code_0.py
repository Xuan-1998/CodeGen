import sys

n = int(input())
arr = list(map(int, input().split()))
dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    for j in range(i):
        if dp[j] and arr[j] >= i - j:
            dp[i] = True
            break

print(dp[-1])
