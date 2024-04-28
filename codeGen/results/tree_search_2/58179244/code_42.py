from collections import defaultdict

n = int(input())
colors = input()

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    prev_color = (colors[i - 1] == 'R') * 2 - 1
    if colors[i - 1] == colors[i - 2]:
        dp[i][prev_color] += 1
    for j in range(3):
        if j != prev_color:
            dp[i][j] = min(dp[i][j], dp[i - 1][j]) + (j == prev_color) * 1

r, t = 0, ''
for i in range(n, 0, -1):
    r += str(min(range(3), key=lambda j: dp[i][j]))
    t = colors[i - 1] if dp[i][ord(colors[i - 1]) - ord('R')] == dp[i][ord(colors[i - 1]) - ord('G')] else 'G' if dp[i][ord(colors[i - 1]) - ord('G')] < dp[i][ord(colors[i - 1]) - ord('B')] else 'B'
    print(t, end='')
print()
