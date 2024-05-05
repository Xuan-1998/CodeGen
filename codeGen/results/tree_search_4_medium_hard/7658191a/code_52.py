def maxScore(k, z, arr):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(k+1)]

    # Base cases
    dp[0][0] = 0
    for i in range(1, n+1):
        dp[0][i] = 0

    for i in range(1, k+1):
        dp[i][0] = 0

    # Fill up the table
    for i in range(1, min(k+1, n)+1):
        for j in range(1, min(i+z+1, n)+1):
            if i < z:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + arr[j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1] + arr[j-1], dp[i-1][j] - arr[j-2])

    return dp[k][n]

# Read input
t = int(input())
for _ in range(t):
    k, z, n = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxScore(k, z, arr))
