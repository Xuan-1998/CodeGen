dp = [[False, False] for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    dp[i][0] = (s[i-1] == 'A' and s[i-2] == 'B') or dp[i-1][1]
    dp[i][1] = (s[i-1] == 'B' and s[i-2] == 'A') or dp[i-1][0]

print('YES' if dp[-1][0] and dp[-1][1] else 'NO')
