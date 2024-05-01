===

n = int(input())
s = input()

dp = {1: [(0, [2**-1])]}
memo = {}

def get_winning_teams(i):
    if i not in memo:
        memo[i] = []
        for j in range(i):
            if s[j] == '1':
                winning_teams = 2**(i-1)
            else:
                winning_teams = sum(dp[j][k][0] for k in range(len(dp[j])))
            memo[i].append(winning_teams)
    return memo[i]

print(sorted(set([j[1] for i in range(1, n+1) for j in get_winning_teams(i)])))
===
