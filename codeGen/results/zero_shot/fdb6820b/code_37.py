m = int(input())
n = int(input())
arr = list(map(int, input().split()))
mod = 10**9 + 7
dp = [0] * (n + 1)
for x in arr:
    for i in range(n, x - 1, -1):
        dp[i] += dp[i-x]
        dp[i] %= mod

print(dp[n])
