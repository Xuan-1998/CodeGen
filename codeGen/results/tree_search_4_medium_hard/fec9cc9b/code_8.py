import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1

for _ in range(m):
    l, r = map(int, input().split())
    if any(dp[l-1] <= dp[i] for i in range(l, r+1)):
        print("Yes")
    else:
        print("No")
