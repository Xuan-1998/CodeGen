def count_portals():
    n = int(input())
    portals = list(map(int, input().split()))
    
    # Initialize dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: Vasya starts at room 1 and needs to get to room n+1
    dp[0][1] = 1
    
    # Fill the rest of the dp[] array based on the recurrence relation
    for i in range(1, n + 1):
        if portals[i - 1]:
            dp[i][portals[i - 1]] = dp[i - 1][1] + 1
        else:
            dp[i][1] = dp[i - 1][1]
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][0]) % 2 + dp[i - 1][0]
    
    # The final answer is the minimum number of portal moves needed to get out of the maze
    return min(dp[n][1], dp[n][0]) % 1000000007

print(count_portals())
