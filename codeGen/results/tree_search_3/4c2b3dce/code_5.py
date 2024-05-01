import sys

dp = [[False] * 2 for _ in range(2 * (len(s) + 1))]

for i in range(len(s)):
    if s[i] == 'A':
        dp[0][1], dp[1][1] = dp[1][1], False
    elif s[i] == 'B':
        dp[0][1], dp[1][0] = False, dp[0][0]

for j in range(2):
    if (j > 0 and (dp[j][0] or dp[j][1])) and not (dp[(j+1)%2][0] or dp[(j+1)%2][1]):
        print("YES")
        sys.exit()

print("NO")
