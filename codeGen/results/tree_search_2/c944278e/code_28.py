import sys

def count_winning_teams(n):
    # Initialize a list to store the number of winning teams for each score
    dp = [0] * (2**n + 1)
    dp[0] = 1  # The team with score 0 is always a winner

    for i in range(1, 2**n):
        total_score = sum((s >> j & 1) for j in range(n))
        if (total_score % 2 == int(s[-1])):
            dp[i] += dp[total_score]
        else:
            dp[i] += dp[total_score - 1]

    return sum(1 for score in range(2**n + 1) if dp[score])

# Read input
n = int(sys.stdin.readline())

# Count the winning teams
winning_teams = count_winning_teams(n)

# Print the output
print(winning_teams)
