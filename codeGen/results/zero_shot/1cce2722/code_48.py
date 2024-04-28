n = int(input())
a = list(map(int, input().split()))
dp = [[0] * 105 for _ in range(2)]
for i in range(n):
    dp[i % 2][a[i]] += 1
res = max(max(dp[0]), max(dp[1]))
print(res)
