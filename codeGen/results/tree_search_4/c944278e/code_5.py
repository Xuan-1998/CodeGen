def any_team_lost_in_phase(phase):
    # Check if at least one team lost in the current phase
    for team in range(2**phase):
        if bin(team)[2:].count('1') < 2**(phase-1):
            return True
    return False

n = int(input())
s = input()

dp = [[False] * (2**n) for _ in range(n)]

for i in range(n):
    for j in range(2**n):
        if s[i] == '1':
            dp[i][j] = True
        else:
            dp[i][j] = any_team_lost_in_phase(i)
        if i > 0:
            dp[i][j] |= dp[i-1][j]

winning_teams = [i for i in range(2**n) if dp[n-1][i]]
print(*sorted(winning_teams), sep='\n')
