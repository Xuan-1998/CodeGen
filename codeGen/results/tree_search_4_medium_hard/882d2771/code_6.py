code = '''
t, l, r = map(int, input().split())
dp = [[[0] * (r - l + 1) for _ in range(l)] for _ in range(t)]

for n in range(1, t+1):
    for k in range(n-1, -1, -1):
        dp[n][k][l] = float('inf')
        for m in range(k+1, n+1):
            dp[n][k][l] = min(dp[n][k][l], 1 + dp[m][k][l])
        if k == l:
            dp[n][k][l] = 0

result = (t*(dp[t][l-1][l-1]) - l*dp[t][r-1][r-1]) % (10**9 + 7)
print(result)
'''

print(code)
