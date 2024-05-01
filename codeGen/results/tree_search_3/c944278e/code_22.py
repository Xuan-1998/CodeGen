from collections import deque

n = int(input())
s = input()

dp = [[False]*2**n for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(2**i):
        if (j & (1 << (i-1))) > 0:  # If the bit at position i-1 is set
            dp[i][j] = True if s[i-1] == 'W' or not dp[i-1][j >> 1] else False
        else:
            dp[i][j] = True if s[i-1] == 'L' or not dp[i-1][j << 1] else False

winning_teams = set()
for j in range(2**n):
    if dp[n][j]:
        winning_teams.add(j)

print('\n'.join(map(str, sorted(list(winning_teams)))))
