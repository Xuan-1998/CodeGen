def find_winning_teams(n):
    # Base case: when n = 1, there is only one team that can win.
    if n == 1:
        return [0]

    # Initialize a table to store the winning teams for each round.
    winning_teams = [[[] for _ in range(2**n)] for _ in range(n)]

    # Iterate through each round.
    for i in range(n):
        # For each team, calculate its skill level based on the result of the current round.
        for j in range(2**i):
            if (j >> (i-1)) & 1:  # Team wins this round
                winning_teams[i][j] = [k for k in winning_teams[i-1][j][0] if winning_teams[i-1][j][1][k]] + [j]
            else:  # Team loses this round
                winning_teams[i][j] = [k for k in winning_teams[i-1][j][0] if not winning_teams[i-1][j][1][k]]

    # Initialize a set to store all the winning teams.
    all_winning_teams = set()

    # Iterate through each round and add the winning teams to the set.
    for i in range(n):
        for j in range(2**i):
            if winning_teams[i][j]:
                all_winning_teams.update(winning_teams[i][j])

    # Sort the winning teams in ascending order.
    return sorted(list(all_winning_teams))

# Read input from stdin
n = int(input())

# Call the function and print the result to stdout
print(find_winning_teams(n))
