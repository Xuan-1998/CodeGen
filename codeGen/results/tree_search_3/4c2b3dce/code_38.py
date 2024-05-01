import sys

n = int(input())
s = input()

dp = [[0, 0] for _ in range(n + 1)]

for i in range(n):
    if s[i] == 'A':
        dp[i+1][0], dp[i+1][1] = dp[i][0], dp[i][1] + 1
    elif s[i] == 'B':
        dp[i+1][0], dp[i+1][1] = dp[i][0] + 1, dp[i][1]

for i in range(n):
    if dp[n][0] == 1 and dp[n][1] == 1:
        print("YES")
        sys.exit(0)

print("NO")
