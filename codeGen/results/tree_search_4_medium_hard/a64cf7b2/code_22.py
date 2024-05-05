import sys

def solve(n, m, T):
    # Initialize the DP table with zeros
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    # Initialize the memoization table with None
    memo = [[None] * (T + 1) for _ in range(n + 1)]

    # Fill up the DP table and memoization table using a bottom-up approach
    for i in range(2, n + 1):
        for t in range(T + 1):
            if (i - 1) * T >= t:
                dp[i][t] = max(dp[j][min(t - w, T)] + 1 for j in range(i - 1)
                                if (j - 1) * T >= w and (memo[j][w] is None or memo[j][w][0] <= i))
                memo[i][t] = dp[i][t]
            else:
                dp[i][t] = dp[i-1][T]

    # Find the maximum number of vertices that can be visited within T time units
    max_vertices = 0
    t = T
    for i in range(n, 0, -1):
        if dp[i][t] > max_vertices:
            max_vertices = dp[i][t]
            route = [i]

            # Reconstruct the route from vertex i to vertex 1
            while True:
                t -= w
                for j in range(i - 1, -1, -1):
                    if (j - 1) * T >= t and memo[j][w] is not None:
                        i = j
                        break
                route.append(i)
        t -= w

    return max_vertices, len(route), route[::-1]
