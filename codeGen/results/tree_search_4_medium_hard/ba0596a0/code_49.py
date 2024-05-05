code
k = int(input())
stones = [int(x) for x in input().split()]
dp = [False] * (max(stones) + 1)

dp[0] = True

for i in range(1, max(stones) + 1):
    if stones[i - 1] > 0 and dp[i - 1]:
        dp[i] = True
    elif stones[i - 1] % (k * 2 + 1) == 0 and i // k >= 0:
        dp[i] = dp[stones[i - 1] // k]
print(dp[-1])
