n = int(input())
s = input()

dp = [[False] * (1 << n) for _ in range(n)]
winning_teams = set()

for i in range(n):
    for j in range(1 << n):
        if dp[i][j]:
            if s[i] == '1':
                dp[i+1][j] = True
            else:
                for k in range(n):
                    if ((j >> k) & 1) and not (s[:i].count('0') % 2 == 0):
                        dp[i+1][j^(1<<k)] = True

for j in range(1 << n):
    if dp[n-1][j]:
        winning_teams.add(j)

print('\n'.join(map(str, sorted(list(winning_teams)))))
