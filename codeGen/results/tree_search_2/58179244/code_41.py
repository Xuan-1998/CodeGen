from sys import stdin

n = int(stdin.readline())
s = stdin.readline().strip()

dp = [[0, 0, 0, float('inf')] for _ in range(n + 1)]

for i in range(1, n + 1):
    if s[i - 1] == s[i - 2]:
        dp[i][2] = min(dp[i][2], dp[i - 1][0])
    else:
        dp[i][0] = dp[i - 1][2]

r = dp[n][0]
t = ''.join(['R' if i % 3 == 0 else 'G' if i % 3 == 1 else 'B' for i in range(n)])

print(r)
print(t)
