def longest_increasing_subsequence(array):
    n = len(array)
    dp = [[1] * n for _ in range(n)]
    
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i][j] = dp[j][i-1] + 1
    
    return max(max(row) for row in dp)
