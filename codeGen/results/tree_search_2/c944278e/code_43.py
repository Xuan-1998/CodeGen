from itertools import combinations

def winning_teams(n):
    memo = {}
    def winning_teams_recursive(s, teams):
        if s in memo:
            return memo[s]
        result = []
        for i in range(len(teams)):
            team = ''.join([str(int(b)) for b in teams[:i+1]])
            if all(int(c) == 1 for c in s[len(team):]):
                result.append(team)
        memo[s] = result
        return result

    winning_teams_recursive('0' * n, list(map(str, range(2**n))))[0]
