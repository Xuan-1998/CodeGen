from collections import deque

def find_min_edges(n, roads):
    # Initialize dp array with infinity values
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Capital city has distance 0 from itself

    def memoized_distance(city):
        if dp[city] == float('inf'):
            for parent in range(1, city):
                if roads[parent - 1][1] == city:
                    # Recursively calculate the shortest distance
                    dp[city] = min(dp[city], 1 + memoized_distance(parent))
                    break
        return dp[city]

    # Fill up dp array using memoized function
    for i in range(2, n + 1):
        memoized_distance(i)

    # Find the city with the maximum distance from the capital
    max_distance_city = max(range(1, n + 1), key=lambda x: dp[x])

    # Count the minimum number of edges to be reversed
    min_edges = sum(1 for i in range(n - 1) if roads[i][0] < roads[i][1] and dp[roads[i][1]] > dp[roads[i][0]])

    return [min_edges, list(range(1, n + 1)) if max_distance_city == 1 else [max_distance_city]]

# Example usage
n = int(input())
roads = []
for _ in range(n - 1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

result = find_min_edges(n, roads)
print(result[0])
print(*result[1], sep='\n')
