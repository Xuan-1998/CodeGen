def vasya_portal_moves():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    crosses = 0
    
    for i in range(2, n + 1):
        if crosses % 2 == 1:
            dp[i] = min(dp[p[i - 1]]) + 1
        else:
            dp[i] = dp[i - 1] + 1
        crosses += (crosses % 2) * 2 + 1
    
    print(dp[-1])  # Print the minimum moves required to get out of the maze

vasya_portal_moves()
