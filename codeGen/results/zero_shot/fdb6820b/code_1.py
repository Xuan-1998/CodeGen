m = int(input())
N = int(input())
nums = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[0] = 1
for num in nums:
    for i in range(N + 1):
        dp[i] += dp[min(i, num)]
print(dp[N] % (10**9 + 7))
