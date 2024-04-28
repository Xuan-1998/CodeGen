code
n = int(input())
colors = input()

dp = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 1 + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = 1 + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = 1 + min(dp[i-1][0], dp[i-1][1])

r = dp[n][colors.index(colors[0])]
print(r)
t = ''.join('R' if i % r == 0 else c for i, c in enumerate(colors))
print(t)

endcode
