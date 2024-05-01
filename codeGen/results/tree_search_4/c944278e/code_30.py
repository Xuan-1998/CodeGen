import sys

def solve(n, s):
    memo = {}
    result = set()

    def dfs(i, s):
        if (i, s) in memo:
            return memo[(i, s)]

        winning_teams = set()
        for j in range(2**n):
            team_skill = format(j, 'b').zfill(n)
            wins = sum(c1 == c2 and c1 == '1' for c1, c2 in zip(team_skill, s))
            if wins >= i:
                winning_teams.add(f"Team {team_skill}")

        memo[(i, s)] = winning_teams
        return winning_teams

    for i in range(n):
        result.update(dfs(i + 1, s[:i + 1]))

    return sorted(list(result))

n = int(input())
s = input()
print(solve(n, s))
