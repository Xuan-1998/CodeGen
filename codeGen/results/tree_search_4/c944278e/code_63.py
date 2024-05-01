def win_teams(n):
    dp = {0: [0]}
    for i in range(1 << n):  # loop through all possible phases
        new_teams = []
        for j in range(i + 1):
            winning_team = list(dp[i ^ (1 << j)].copy())
            if s[j]:  # current team wins
                winning_team.append(j)
            else:  # current team loses
                winning_team.sort()
            dp[i] = list(set(winning_team))
        if i == (1 << n) - 1:
            return sorted(dp[i])
    return []

n = int(input())
s = input().split()
print(win_teams(n))
