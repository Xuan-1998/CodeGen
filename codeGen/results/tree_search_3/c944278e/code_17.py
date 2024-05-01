import sys

n = int(input())
dp = [0] * (n + 1)
s = input()

for i in range(n - 1, -1, -1):
    win = True
    for j in range(i):
        if s[j] == '1':
            win = False
            break
    dp[i] = dp[i + 1]
    if win:
        dp[i] += 1

winning_teams = [str(2 ** i - dp[i]) for i in range(n)]
print(' '.join(winning_teams))
