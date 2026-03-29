# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Initialize the total number of players and the number of players in the department of interest
total_players = sum(s)
players_in_interest_dept = s[h-1]

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
if n > total_players:
    print(-1)  # If there are not enough basketball players in the university to form a team, output -1 instead.
else:
    prob = sum(min(n, si) / (n * s_i) for s_i in s) if h else sum(min(n, si) / n for si in s)
    print(prob)

