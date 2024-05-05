n, q = map(int, input().split())
signs = list(input())

dp = [[float('inf')] * (q + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(q):
        if signs[i] == '+':
            dp[i][j] = min(dp[i-1][j], 1)
        else:
            dp[i][j] = min(dp[i-1][j], 2)

for _ in range(q):
    l, r = map(int, input().split())
    total_signs = sum(1 for sign in signs[l:r+1] if sign == '+') - sum(1 for sign in signs[l:r+1] if sign == '-')
    dp[n][r] = min(dp[n-1][l-1] + total_signs, 0)
    print(min(dp[n][r], 0), end='\n')
