def winning_teams(n):
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            result = [(1, 0)] + dfs(1, 0)
        elif j > i:
            result = [(0, 1)] + dfs(0, 1)
        else:
            result = []
        memo[(i, j)] = result
        return result

    teams = [i for i in range(2**n)]
    winning_teams = set()
    for team in teams:
        result = ''.zfill(n)
        skill_levels = [(team >> i) & 1 for i in range(n)]
        for match in range(n):
            if result[match] == '0':
                if skill_levels[match]:
                    result = '1' + result[:match]
                else:
                    result = '0' + result[:match]
        winning_teams.update(dfs(*skill_levels))

    return sorted(list(winning_teams))
