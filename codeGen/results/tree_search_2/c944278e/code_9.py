from itertools import combinations

def find_winning_teams(n):
    # Initialize an empty set to store the winning teams
    winning_teams = set()

    # Generate all possible permutations of teams
    for r in range(1, 2**n + 1):
        for team in combinations(range(2**n), r):
            # Convert the permutation into a binary string
            perm_str = ''.join(str(int(i in team)) for i in range(2**n))

            # Check if the permutation is a winning team
            if perm_str == ''.join(map(str, sorted([int(x) for x in perm_str]))):
                # Add the winning team to the set
                winning_teams.add(tuple(sorted(team)))

    # Sort the winning teams and print them
    for team in sorted(winning_teams):
        print(' '.join(map(str, team)))

n = int(input())
find_winning_teams(n)
