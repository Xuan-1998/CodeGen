import sys

def solve(n, s):
    dp = [[False] * (1 << n) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for mask in range(1 << i):
            if dp[i - 1][mask]:
                dp[i][mask | (1 << (i - 1))] = True
            for j in range(i):
                if not (s[j] & (1 << (i - 1))):
                    dp[i][mask ^ (1 << j)] = True

    winning_teams = []
    for i in range(1 << n):
        if dp[n][i]:
            winning_teams.append(bin(i)[2:].zfill(n))

    return sorted(winning_teams)

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip()))

print(*solve(n, s), sep='\n')
