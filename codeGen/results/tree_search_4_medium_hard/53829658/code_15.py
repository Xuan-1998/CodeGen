from collections import deque
import sys

# Read input
n = int(input())
capital = 0
roads = []
for i in range(n-1):
    road = list(map(int, input().split()))
    roads.append((road[0], road[1]))

# Perform BFS from each city to find the shortest distance to the capital
dp = [sys.maxsize] * (n+1)
for city in range(1, n+1):
    queue = deque([(city, 0)])  # Initialize a BFS queue with city and distance
    while queue:
        curr_city, dist = queue.popleft()
        if curr_city == capital:  # If we've reached the capital, update dp
            for neighbor in roads:
                if neighbor[1] == curr_city:
                    dp[neighbor[0]] = min(dp[neighbor[0]], dist + 1)
        else:  # Perform BFS to find neighbors of current city
            for neighbor in roads:
                if neighbor[1] == curr_city and dp[neighbor[0]] > dist + 1:
                    queue.append((neighbor[0], dist + 1))
    # Update dp with the shortest distance from capital to each city
    dp = [min(dp[i+1], i) for i in range(n)]

# Calculate the minimum number of reversed edges needed to reach any other city from the capital
reversed_edges = max(dp[1:])

# Print the solution
print(reversed_edges)
capital_cities = [i+1 for i in range(n) if dp[i+1] == i]
print(*capital_cities, sep=' ')
