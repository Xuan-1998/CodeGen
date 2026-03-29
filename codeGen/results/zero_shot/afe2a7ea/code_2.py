import sys
from collections import defaultdict

# Input n
n = int(sys.stdin.readline())

# Create a hashmap to store the number of towns that can be reached by each town
towns_reached = defaultdict(int)
for i in range(1, n+1):
    towns_reached[i] += 1
    if i > 1:
        towns_reached[i-1] += 1
    if i < n:
        towns_reached[i+1] += 1

# Calculate the number of ways to reach each town
ways_to_reach = [0]*(n+2)
for i in range(1, n+1):
    ways_to_reach[i] = ways_to_reach[i-1] + ways_to_reach[i+1]
ways_to_reach[0] = 1

# Calculate the number of ways to reach each town
towns_reached_values = [0]*(n+2)
for i in range(1, n+1):
    towns_reached_values[i] = (ways_to_reach[i-1] + ways_to_reach[i+1]) % 998244353

# Calculate the probability of finding a way to set signal powers
probability = 1
for i in range(1, n+1):
    probability *= towns_reached_values[i]

print(probability % 998244353)
