def min_mana(monitor_appearance_time, monitor_health):
    n = len(monitor_appearance_time)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the base case: no monsters to kill
    for i in range(1, n + 1):
        dp[i][i] = monitor_health[i - 1]
    
    # Fill up the dynamic programming table
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length
            
            dp[end][end] = max(dp[start][end])
            
            for i in range(start + 1, end + 1):
                if monitor_health[i - 1] > dp[i - 1][start]:
                    dp[end][end] = min(dp[end][end], monitor_health[i - 1] + dp[i - 1][i - 1])
    
    return dp[-1][-1]

# Read input from standard input
n = int(input())
monitor_appearance_time = list(map(int, input().split()))
monitor_health = list(map(int, input().split()))

print(min_mana(monitor_appearance_time, monitor_health))
