def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[1] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = max(dp[i][j], dp[j][i-1] + 1)
    
    return max(max(row) for row in dp)

# Read input from stdin
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
