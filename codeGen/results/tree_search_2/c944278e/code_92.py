def find_winning_teams(n, s):
    # Initialize the DP table with 0s
    dp = [0] * (1 << n)

    # Iterate through each possible phase outcome
    for i in range(2**n):
        skill_level = 0
        # Calculate the skill level of the current set of winning teams
        for j in range(n):
            if ((i >> j) & 1):  # Team j wins
                skill_level += 2 ** (n - j - 1)
        # Update the DP table based on possible outcomes
        for k in range(2**n):
            new_skill_level = skill_level
            # If team j loses, subtract its skill level from the total
            for j in range(n):
                if ((k >> j) & 1):  # Team j wins
                    new_skill_level -= 2 ** (n - j - 1)
            dp[k] = max(dp[k], dp[i] + new_skill_level)

    # Find all winning teams by iterating through the DP table
    winning_teams = []
    for i in range(2**n):
        if dp[i] > 0:
            skill_level = 0
            for j in range(n):
                if ((i >> j) & 1):  # Team j wins
                    skill_level += 2 ** (n - j - 1)
            winning_teams.append(skill_level)

    return sorted(winning_teams)

# Example usage
n = int(input())
s = input()
print(find_winning_teams(n, s))
