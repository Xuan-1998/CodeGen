def min_replantings():
    n, m = map(int, input().split())
    
    dp = [[0] * m for _ in range(n + 1)]
    last_seen = [0] * (m + 1)
    
    for i in range(1, n + 1):
        s_i, x_i = map(int, input().split())
        
        # Find the maximum index such that x_k < x_i
        k = max(j for j in range(m) if last_seen[j] <= x_i)
        
        # Calculate the minimum number of replantings for plants up to and including ith plant
        if s_i == 1:
            dp[i][s_i - 1] = 0
        else:
            for section in range(s_i - 1, m):
                if k < s_i:
                    dp[i][section] = dp[k][section - 1]
                else:
                    dp[i][section] = min(dp[k][j] + (s_i != j) for j in range(1, s_i)) or 0
        
        # Update the last seen position for each species
        last_seen[s_i - 1] = x_i
    
    return sum(sum(row) for row in dp)
