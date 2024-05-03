def min_replants(n, m):
    dp = {(i, 0): i for i in range(1, m+1)}  # Base case: all plants replanted
    for _ in range(n):
        last_species, total_replanted = sorted(dp.items())[-1]  # Get the state with the most recently replanted species
        dp[last_species, total_replanted + 1] = (last_species, total_replanted + 1)
        if last_species < m:
            dp[m, total_replanted + 1] = (m, total_replanted + 1)
    return min(dp.values())  # Return the minimum number of plants that need to be replanted
