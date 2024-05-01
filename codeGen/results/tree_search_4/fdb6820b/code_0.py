def countWays(arr, n):
    m = len(arr)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: there's only one way to form 0 with any subset of the first i elements.
    for i in range(m + 1):
        dp[i][0] = 1
    
    # Fill up the dp table by iterating over N from 1 to n and i from 1 to m:
    for N in range(1, n + 1):
        for i in range(1, m + 1):
            if arr[i - 1] <= N:
                for j in range(i):
                    dp[N][i] = (dp[N][i] + dp[max(0, N - arr[j])][j]) % (10**9 + 7)
    
    return dp[n][m]

# Read input from standard input
m, n = map(int, input().split())
arr = list(map(int, input().split()))

print(countWays(arr, n))
