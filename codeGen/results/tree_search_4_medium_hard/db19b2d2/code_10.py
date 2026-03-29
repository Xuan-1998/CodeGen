import math

def prob_at_least_one_from_department(n, m, h, s):
    # Calculate the total number of possible teams
    total_teams = math.factorial(m + n - 1) // (math.factorial(n) * math.factorial(m - 1))

    # Initialize dp array with zeros
    dp = [0] * (h + 1)

    # Base case: initially no player from the department of interest
    dp[0] = 1

    for i in range(1, h + 1):
        # Calculate the probability that a team has exactly i players from the department of interest
        dp[i] = min(dp[i - 1] * sum(sj <= i for sj in s) / total_teams, 1)

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob_at_least_one = sum(dp[i] for i in range(1, h + 1))

    return prob_at_least_one

# Example usage:
n = int(input())  # number of players on the team
m = int(input())  # number of departments in the university
h = int(input())  # department of interest
s = list(map(int, input().split()))  # number of basketball players in each department

print(prob_at_least_one_from_department(n, m, h, s))
