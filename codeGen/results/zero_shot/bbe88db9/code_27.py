code
n = int(input())
p = list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(1, n+1):
    if dp[i-1] % 2 == 0:
        dp[i] = (dp[i-1] + 1) % 1000000007
    else:
        dp[i] = dp[i-1] % 1000000007

print(dp[n])
