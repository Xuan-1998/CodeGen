def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize dp array with size (n+1) * (n+1)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case: There is only one way to form an empty subsequence, which is to not select any elements.
    for i in range(1, n+1):
        dp[i][0] = 1
    
    # Fill up the dp array
    for length in range(1, n+1):
        for end in range(length, n+1):
            if a[end-1] % length != 0:
                dp[length][end] = dp[length][end-1]
            else:
                dp[length][end] = (dp[length-1][end-1] + dp[length][end-1]) % (10**9 + 7)
    
    # The number of good subsequences is stored in the last cell of the dp array
    return dp[n][n]

print(solve())
