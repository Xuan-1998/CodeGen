def max_gasoline(n, w, roads):
    # Initialize memoization array
    dp = [0] * n

    def dfs(city):
        if dp[city] > 0: return dp[city]
        for road in roads:
            if road[0] == city:
                dest, length = road[1], road[2]
                if w[city] - length >= 0:
                    dp[city] = max(dfs(dest), w[city] - length)
                else: break
        return dp[city]

    # Calculate maximum gasoline for each city and store in memoization array
    for i in range(n):
        dfs(i)

    # Return maximum gasoline at the end of the path
    return max(dp)

# Example usage:
n = int(input())  # Number of cities
w = list(map(int, input().split()))  # Maximum amount of gasoline available at each city
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, (v, c)))

print(max_gasoline(n, w, roads))
