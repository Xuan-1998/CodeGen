# Define the variables
n = int(input())  # Number of players on the team
m = int(input())  # Number of departments in the university
h = int(input())  # Department of interest
s = list(map(int, input().split()))  # Number of basketball players in each department

# Calculate the total number of basketball players
total_players = sum(s)

# Check if there are enough basketball players to form a team
if total_players < n:
    print(-1)  # If not, output -1
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 1 - (n-1) / (total_players - s[h-1]) if total_players > n else 0
    print(prob)
