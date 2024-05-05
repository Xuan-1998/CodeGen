import sys

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Initialize DP table with zeros
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(min(i - 1, k) + 1):
            if j < z:
                dp[i][j] = max(dp[i-1][j-1] + arr[i-1], dp[i-1][j] + arr[i])
            else:
                dp[i][j] = dp[i-1][j] + arr[i]
    
    # The maximum score is the last element of the DP table
    print(max(dp[-1]))
