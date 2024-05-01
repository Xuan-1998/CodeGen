===BEGIN CODE===
n = int(input())
s = input()

dp = [[False] * (1 << n) for _ in range(n)]

for i in range(n):
    for j in mask:
        if s[i] == '1' and ((mask >> i) & 1):
            dp[i][j] = True
        elif i == n - 1:
            dp[i][j] = (s[i] == '1')

winning_teams = [team for i, team in enumerate(bin((1 << n) - 1)[2:].zfill(n)):
                 bit_mask := int(team, 2)
                 all_win = True
                 for j in range(n):
                     if not dp[j][bit_mask >> j & 1]:
                         all_win = False
                         break
                 if all_win:
                     print(i)

===END CODE===
