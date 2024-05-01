import sys

def find_winning_teams(n):
    # Read the binary string from stdin
    s = [int(x) for x in sys.stdin.readline().strip().split()]

    # Initialize an empty list to store the winning teams
    winning_teams = []

    # Calculate the cumulative skill levels of each team based on the outcomes
    team_skill_levels = [0] * (2 ** n)
    for i in range(n):
        for j in range(2 ** i, 2 ** (i + 1)):
            if s[i] == 1:
                team_skill_levels[j] += 1
            else:
                team_skill_levels[j] -= 1

    # Find the winning teams by comparing their total skill levels
    for i in range(len(team_skill_levels)):
        if team_skill_levels[i] > 0:
            winning_teams.append(i)

    # Sort the winning teams in ascending order and print them to stdout
    winning_teams.sort()
    for team in winning_teams:
        sys.stdout.write(f"{team}\n")

# Read the value of n from stdin and call the function
n = int(sys.stdin.readline().strip())
find_winning_teams(n)
