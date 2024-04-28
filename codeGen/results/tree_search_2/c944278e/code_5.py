import sys

n = int(sys.stdin.readline())
dp = [0] * (1 << n)

for i in range(1, 1 << n):
    for j in range(n):
        if ((i >> j) & 1):  # team j wins
            dp[i] = max(dp[i], dp[(i - 1) // 2] + 1)
        else:  # team j loses
            dp[i] = max(dp[i], dp[i // 2])

winning_teams = []
for i in range(1, 1 << n):
    if dp[i] == dp[-1]:
        winning_teams.append(i)

print(*sorted(winning_teams))
