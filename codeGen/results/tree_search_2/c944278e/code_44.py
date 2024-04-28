import itertools

def winning_teams(n):
    # Read the input binary string from stdin
    s = input()

    # Generate all possible subsets of teams
    teams = [i for i in range(2**n)]
    subsets = list(itertools.chain(*[list(map(int, bin(i)[2:].zfill(n))) for i in range(2**n)]))

    # Initialize the winning teams list
    winning_teams = []

    # Iterate over all subsets and calculate their skill levels
    for subset in subsets:
        team_skills = [int(s[i], 2) * (1 if bit == '1' else -1) for i, bit in enumerate(bin(subset)[2:].zfill(n))]
        total_skill = sum(team_skills)

        # Check if the subset can win the tournament
        if total_skill > max(winning_teams, default=0):
            winning_teams = [subset]

    # Print the winning teams to stdout
    for team in sorted(set(winning_teams)):
        print(f"Team {team}")
