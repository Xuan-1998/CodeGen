from bitstring import BitArray

n = int(input())  # Read n from stdin
s = BitArray(int_val=int(input()), length=n)  # Read s from stdin

dp = [[set() for _ in range(2**i)] for i in range(n+1)]

for k in range(n):
    for j in range(2**k):
        if s[k] == '1':
            dp[k+1][j|(1<<k)] |= dp[k][j>>1<<k]
        else:
            dp[k+1][j^(1<<k)] -= dp[k][j>>1<<k]

winning_teams = set()
for j in range(2**n):
    winning_teams |= dp[n][j]

print(' '.join(map(str, sorted(winning_teams))))
