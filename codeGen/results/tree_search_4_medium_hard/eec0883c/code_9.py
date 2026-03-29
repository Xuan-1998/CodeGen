import sys

def max_gas(n, w, roads):
    dp = [[0] * (w[i] + 1) for i in range(n)]

    # Base case: Nut starts with the initial amount of gas at each city.
    for i in range(n):
        dp[i][w[i]] = w[i]

    # Recursive relation: For each road (u, v, c), update dp[v][k] for k in range(dp[u][c], 0]:
    for u, v, c in roads:
        for j in range(c + 1):
            if j >= c:
                for k in range(c - 1, -1, -1):
                    if k >= c and dp[u][k] >= c:
                        dp[v][j - c] = max(dp[v][j - c], dp[u][k] - c)
            else:
                dp[v][j] = max(dp[v][j], dp[u][j])

    return max(max(row) for row in dp[-1])

# Input
n = int(input())
w = [int(x) for x in input().split()]
roads = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    roads.append((u - 1, v - 1, c))

print(max_gas(n, w, roads))
