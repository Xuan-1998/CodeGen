import sys

n = int(sys.stdin.readline())
s = bin(int(sys.stdin.readline().strip()))[2:].zfill(n)

dp = [[0] * (1 << n) for _ in range(n + 1)]

for i in range(n, -1, -1):
    for mask in range(1 << (n - i)):
        if s[i-1] == '1':
            dp[i][mask | (1 << (n - i))] += dp[i-1][mask]
        else:
            dp[i][mask] += dp[i-1][mask]

winning_teams = [str(i).zfill(n) for i in range(1 << n) if dp[n][i]]
print('\n'.join(sorted(winning_teams)))
