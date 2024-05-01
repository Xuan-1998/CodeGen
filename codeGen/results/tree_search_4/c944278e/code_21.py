import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip()))

dp = [[False] * (1 << n) for _ in range(n + 1)]

for i in range(n):
    for j in range(1 << n):
        if s[i] & (1 << (j % (1 << n))):
            if dp[i][j]:
                dp[n - i - 1][j]: True
            else:
                dp[i][j]: False

winning_teams = [i for i in range(1 << n) if dp[n // 2][i]]
print(*sorted(winning_teams), sep='\n')
