# Read the input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Initialize the total number of players and the number of players in the department of interest
total_players = sum(s)
players_in_department_of_interest = s[h-1]

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = 0

for i in range(1, n+1):
    if players_in_department_of_interest >= i:
        probability += (total_players - sum(s[:h-1])) / total_players ** i
    else:
        break

# If there are not enough basketball players in the university to form a team, output -1 instead
if total_players < n:
    print(-1)
else:
    print(probability)
