import itertools

def find_winning_teams(n):
    # Generate all permutations
    perms = list(itertools.permutations([i for i in range(2**n)]))

    # Initialize an empty set to store the winning teams
    winning_teams = set()

    # Iterate over each permutation and check if it's a winning team
    for perm in perms:
        is_winning_team = True

        # Check if any team has been defeated
        for i in range(n):
            if (perm[i] & 1) == 0 and any(perm[j] > perm[i] for j in range(i+1, n)):
                is_winning_team = False
                break

        # If the permutation is a winning team, add it to the set
        if is_winning_team:
            winning_teams.add(tuple(sorted(perm)))

    # Sort and return the winning teams
    return sorted(list(winning_teams))

n = int(input())
print(find_winning_teams(n))
