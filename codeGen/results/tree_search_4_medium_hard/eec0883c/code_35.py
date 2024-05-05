import sys

# Read the number of cities, and the maximum amount of gasoline that Nut can buy in each city.
n = int(sys.stdin.readline().strip())
gasoline_capacities = list(map(int, sys.stdin.readline().split()))

# Read the road system, with each line containing three integers u, v, and c representing two cities connected by a road of length c.
roads = []
for _ in range(n - 1):
    u, v, c = map(int, sys.stdin.readline().split())
    roads.append((u - 1, v - 1, c))

# Initialize the dp table with zeros. The dp[i][j] value will store the maximum amount of gasoline that Nut can have at the end of a path from city 0 to city i with j units of gasoline.
dp = [[0] * (sum(gasoline_capacities) + 1) for _ in range(n)]

# Iterate over all possible paths from the starting city to each other city. For each path, calculate the maximum amount of gasoline that can be achieved by considering the road length and the remaining gasoline.
for u, v, c in roads:
    for j in range(sum(gasoline_capacities) + 1):
        if dp[u][j] > 0:  # If there is a path from city 0 to city u with j units of gasoline.
            dp[v][min(j + c, sum(gasoline_capacities))] = max(dp[v][min(j + c, sum(gasoline_capacities))], dp[u][j])

# Return the value at the last cell of the dp table, which represents the maximum amount of gasoline Nut can have at the end of the path.
print(max(dp[-1]))
