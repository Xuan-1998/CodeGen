import sys

def tournament(s):
    n = len(s)
    dp = [0] * (1 << n)  # Initialize DP table with zeros

    for i in range(1 << n):  # Iterate over all possible states
        if bin(i).count('1') == 1:  # Base case: only one team can win
            dp[i] = int(s[0])  # The skill level of the winning team is s[0]
        else:
            max_skill = 0  # Initialize maximum skill for this state
            for j in range(n):
                mask = (1 << j) - 1  # Mask to check if j-th team has won
                if (i & mask) == mask:  # If the j-th team has won
                    max_skill = max(max_skill, dp[i ^ mask] + int(s[j]))  # Update maximum skill
            dp[i] = max_skill

    winning_teams = []  # Initialize list of winning teams
    for i in range(1 << n):
        if dp[i] > 0:  # If there's a team that can win
            winning_teams.append(dp[i])  # Add the maximum skill level to the list

    return sorted(winning_teams)  # Return the list of winning teams in ascending order

n = int(input())  # Read n from stdin
s = input()  # Read binary string s from stdin

print(" ".join(map(str, tournament(s))))  # Print the winning teams
