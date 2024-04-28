m = int(input())
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[0] = 1
for i in arr:
    for j in range(N // 2, i - 1, -1):
        dp[j] = (dp[j] + dp[j - i]) % (10**9 + 7)
print(dp[N])
