def solve(n, m, T):
    # Initialize dp table with zeros
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    # Base case: when i == 1, the maximum number of vertices that can be visited is 1
    dp[1][0] = 1

    # Iterate over edges leaving vertex i
    for u, v, ti in [list(map(int, input().split())) for _ in range(m)]:
        # Iterate over time t from 0 to T
        for t in range(T + 1):
            if t >= ti:
                # If we have enough remaining time, consider visiting vertex v
                dp[v][t - ti] = max(dp[v][t - ti], dp[u][t])
            else:
                # If we don't have enough remaining time, just copy the value from u
                dp[v][t] = dp[u][t]

    # Return the maximum number of vertices that can be visited starting from vertex 1 and ending at vertex n within time T
    return dp[n][T]
