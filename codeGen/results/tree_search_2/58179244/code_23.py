n = int(input())
s = input()

dp = [[float('inf')] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    if s[i - 1] == 'R':
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + 1
        dp[i][1] = dp[i - 1][0]
        dp[i][2] = dp[i - 1][0]
    elif s[i - 1] == 'G':
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + 1
        dp[i][0] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][1]
    else:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + 1
        dp[i][0] = dp[i - 1][2]
        dp[i][1] = dp[i - 1][2]

r = dp[-1].index(min(dp[-1]))  # minimum number of recolors needed

t = [c for c in s[:]]
for i in range(1, n):
    if t[i - 1] == 'R' and t[i] == 'G':
        t[i] = 'B'
    elif t[i - 1] == 'G' and t[i] == 'B':
        t[i] = 'R'
    elif t[i - 1] == 'B' and t[i] == 'R':
        t[i] = 'G'

print(r)
print(''.join(t))
