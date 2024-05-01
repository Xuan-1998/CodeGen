dp = [[False, False] for _ in range(2)]
for c in s:
    if c == 'A':
        dp[0][0] = True
        dp[1][1] = False
    elif c == 'B':
        dp[0][1] = False
        dp[1][0] = True
print('YES' if any(dp[0]) or any(dp[1]) else 'NO')
