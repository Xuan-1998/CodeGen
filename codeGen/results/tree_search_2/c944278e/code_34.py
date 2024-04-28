import sys

def find_winning_teams(n, s):
    dp = [0] * (1 << n)  # Initialize dynamic programming array
    max_score = 0

    for i in range(n):  # Process each phase of the tournament
        mask = (1 << i)
        for j in range(len(s)):
            if s[j] == '1':
                dp[mask | (1 << j)] += 2 ** (n - i - 1)  # Update scores ahead
            else:
                dp[mask | (1 << j)] -= 2 ** (n - i - 1)  # Update scores behind or equal

        max_score = max(max_score, max(dp))  # Find the maximum score at the end of each phase

    winning_teams = [i for i in range(len(s)) if dp[1 << i] == max_score]  # Find teams with the maximum score
    return winning_teams

# Example usage:
n = int(input())
s = input()
print(*find_winning_teams(n, s), sep='\n')
