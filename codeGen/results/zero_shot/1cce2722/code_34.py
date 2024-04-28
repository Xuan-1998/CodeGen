n = int(input())
a = list(map(int, input().split()))
dp = [0] * (105 + 1)
for x in a:
    dp[x] += 1
ans = sum(min(2*i, n) for i in range(1, 105 + 1)) - max(dp[2], dp[-2]) - sum(min(i, dp[i]) for i in range(1, 105 + 1))
print(ans)
