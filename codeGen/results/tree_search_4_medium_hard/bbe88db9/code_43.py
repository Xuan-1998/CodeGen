def portal_moves():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = {(i, 0): [1] if i == 1 else [0] for i in range(n+2)}
    dp[1][0] = 1
    
    for i in range(1, n+1):
        odd_crosses = dp[i-1][0] % 2 != 0
        if i > 1:
            dp[i][(odd_crosses * 2) - 1].append(i)
        dp[i][1-(odd_crosses * 2)] += sum(dp[i-1][1-(odd_crosses * 2)] for _ in range(2))
    
    return dp[n+1][0] % (10**9 + 7)

print(portal_moves())
