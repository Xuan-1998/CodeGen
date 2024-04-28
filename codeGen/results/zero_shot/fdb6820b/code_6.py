n, m = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(m):
    x = int(input())
    for i in range(x, n + 1):
        dp[i] += 1
print(dp[n] % (10**9 + 7))
