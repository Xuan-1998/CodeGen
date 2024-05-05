def findNumberOfLIS(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            if arr[i] < arr[j - 1]:
                dp[i][j] = max((dp[k][j - 1] or 0) + 1 for k in range(i))
    
    max_length = max(dp[i][n] for i in range(n))
    return sum(1 for i in range(n) if dp[i][n] == max_length)

# Receive input from stdin
arr = list(map(int, input().split()))
print(findNumberOfLIS(arr))
