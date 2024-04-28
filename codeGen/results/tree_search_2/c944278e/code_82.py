from sys import stdin

n = int(stdin.readline())
s = stdin.readline().strip()

# Initialize 2D table dp
dp = [[0] * (1 << n) for _ in range(n + 1)]

for i in range(1, n + 1):
    winning_teams = []
    for j in range(i):
        if s[j] == '1':
            winning_teams.append(1 << j)
    max_wins = 0
    for mask in range(1 << i):
        if sum(1 << j for j in range(n) if (mask & (1 << j)) and s[j] == '1') > max_wins:
            max_wins = sum(1 << j for j in range(n) if (mask & (1 << j)) and s[j] == '1')
    dp[i][0] = max_wins

# Print the winning teams
winning_teams = []
for i in range(n, 0, -1):
    max_mask = 0
    for mask in range(1 << n):
        if dp[i - 1][mask] > dp[i - 1][max_mask]:
            max_mask = mask
    winning_teams.append(bin(max_mask)[2:].zfill(n))
    s = bin(max_mask)[2:]
    for j in range(i - 1, -1, -1):
        if s[j] == '1':
            s = s[:j] + '0' * (n - j) + s[j + 1:]
    dp[i - 1][max_mask] -= sum(1 << j for j in range(n) if s[j] == '1')

print("\n".join(sorted(winning_teams)))
