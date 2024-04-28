import sys

n = int(input())
colors = input()

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 0
    prev_color = colors[0]
    recolors_needed = 0
    for j in range(1, i + 1):
        if colors[j - 1] == prev_color:
            recolors_needed += 1
        else:
            prev_color = colors[j - 1]
        dp[i][recolors_needed] = min(dp[i][recolors_needed], dp[i-1][recolors_needed - 1] + 1)

r = float('inf')
for i in range(n // 2, n):
    if dp[n][i] < r:
        r = dp[n][i]

print(r)
