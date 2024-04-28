import itertools

def winning_teams(n, s):
    # Base case: when no games have been played (all zeros)
    if len(s) == 0:
        return [[i] for i in range(2**n)]

    # Compute the winning teams for each subproblem
    subproblems = []
    for p in itertools.permutations(range(2**n)):
        subproblem_s = ''.join('1' if s[i] == '1' else '0' for i in range(len(s)))
        subproblems.append(winning_teams(n-1, subproblem_s))

    # Combine the winning teams from each subproblem
    winning_teams = set()
    for p in itertools.product(*subproblems):
        team = []
        for game in range(2**n - 1):
            if s[game] == '1':
                team.append(p[game][0])
        winning_teams.add(tuple(sorted(team)))

    return [list(team) for team in winning_teams]

# Example usage
n = int(input())
s = input()
print(winning_teams(n, s))
