import itertools

def solve():
    n = int(input())
    s = input()

    # Generate all permutations of the binary string 's'
    perms = list(itertools.permutations(s))

    # Initialize an empty set to store the winning teams
    winning_teams = set()

    # Iterate over each permutation and calculate its total score
    for perm in perms:
        total_score = 0
        for i, team in enumerate(perm):
            if team == '1':
                total_score += 2 ** (n - i - 1)
        # Add the permutation to the set of winning teams if its score is greater than 0
        if total_score > 0:
            winning_teams.add(tuple(sorted(map(int, perm))))

    # Print the winning teams in ascending order
    for team in sorted(winning_teams):
        print(''.join(map(str, team)))

if __name__ == '__main__':
    solve()
