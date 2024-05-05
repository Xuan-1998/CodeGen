python
import math

def calculate_probability():
    n, m, h = map(int, input().split())  # Read input
    s = list(map(int, input().split()))  # Read number of players in each department
    
    # Check if there are enough basketball players to form a team
    if sum(s) < n:
        return -1  # Output -1 if not enough players

    # Calculate the probability that at least one player from the department of interest is selected
    probability = 0  # Initialize probability to 0
    for i in range(m):
        if i == h:  # If it's the department of interest
            probability += s[i] / sum(s)  # Add the probability of selecting at least one player from this department
        else:
            probability -= s[i] * (1 - math.exp(-s[i]))  # Subtract the probability that we don't select any players from this department
    
    return min(1, probability)  # Ensure the probability is not greater than 1

print(calculate_probability())
