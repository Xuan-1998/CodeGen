def find_winning_teams(n, s):
    # Initialize memoization dictionary
    memo = {}

    def simulate_tournament(teams, phase=0):
        if str(teams) in memo:
            return memo[str(teams)]

        if len(teams) == 1:
            return [teams]

        winning_teams = []
        for i in range(len(teams)):
            team1 = teams[i]
            remaining_teams = teams[:i] + teams[i+1:]
            if s[phase] == '1':
                # Team1 wins, add it to the list of winning teams
                winning_teams.extend(simulate_tournament(remaining_teams, phase+1))
            else:
                # Team2 wins, add it to the list of winning teams
                winning_teams.extend(simulate_tournament([team1] + remaining_teams, phase+1))

        memo[str(teams)] = winning_teams
        return winning_teams

    # Generate all possible permutations of teams and filter out non-winning teams
    winning_teams = set()
    for permutation in itertools.permutations(range(2**n)):
        winning_teams.update(simulate_tournament(permutation))

    # Sort the winning teams in ascending order
    sorted_winning_teams = sorted(list(winning_teams), key=lambda x: 0)

    return sorted_winning_teams

# Read input from stdin
import sys
n, s = map(int, sys.stdin.readline().split())

# Call the function to find all winning teams
winning_teams = find_winning_teams(n, s)

# Print the result to stdout
print(*winning_teams, sep='\n')
