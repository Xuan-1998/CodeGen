import sys

def solve(n):
    # Read the binary string representing the tournament results
    s = input().strip()

    # Initialize a dictionary to store intermediate results
    memo = {}

    def dfs(i, j, skill):
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case: If we've reached the end of the tournament, 
        # the current team is the winning team.
        if i == n:
            return [skill]

        # Initialize a list to store the winning teams
        winning_teams = []

        # Iterate over all possible next matches (0 or 1)
        for bit in range(2):
            # Calculate the skill level of the next team based on the 
            // binary string and XOR operation.
            new_skill = skill ^ (int(s[i], 2) & (1 << bit))

            # Recursively call dfs with the updated skill level
            teams = dfs(i + 1, j + bit, new_skill)

            # If there are any winning teams in this recursive call,
            // add them to our result.
            if teams:
                winning_teams.extend(teams)

        return winning_teams

    # Call the dfs function with the initial skill level (0) and 
    // 0 as the current round (since we're considering all matches).
    teams = dfs(0, 0, 0)

    # Sort the winning teams in ascending order
    teams.sort()

    # Print the result
    print(*teams, sep='\n')

# Read the input value n from standard input
n = int(input())

# Call the solve function with n
solve(n)
