import sys

n = int(sys.stdin.readline())
s = list(map(str, sys.stdin.readline().strip()))

dp = [[False for _ in range(2**n)] for _ in range(n+1)]

for i in range(n):
    for j in range(2**n):
        if s[i] == 'W' and ((j >> i) & 1):
            dp[i+1][j] = True
        else:
            dp[i+1][j] = False

winners = [i for i in range(2**n) if dp[n][i]]

print('\n'.join(map(str, winners)))
