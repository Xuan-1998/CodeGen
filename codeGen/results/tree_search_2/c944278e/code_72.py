import sys

n = int(input())
s = bin(int(input()))[2:].zfill(n)

dp = [[0]*2 for _ in range(2**n)]

for i in range(2**n):
    if n == 1:
        dp[i][int(s)] = s
    else:
        for j in range(2**n):
            if (j >> (n-1)) & 1:
                if dp[j>>1][s[:n-1]] == s[n-1]:
                    dp[j][0] = dp[j>>1][s[:n-1]]
                else:
                    dp[j][0] = 1 - dp[j>>1][s[:n-1]]
            else:
                if dp[j>>1][s[:n-1]] == 1 - s[n-1]:
                    dp[j][1] = dp[j>>1][s[:n-1]]
                else:
                    dp[j][1] = 1 - dp[j>>1][s[:n-1]]

winning_teams = [i for i in range(2**n) if dp[i][-1]]
print('\n'.join(map(str, winning_teams)))
