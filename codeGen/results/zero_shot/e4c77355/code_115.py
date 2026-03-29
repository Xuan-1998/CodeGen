def longest_increasing_subsequence():
    arr = [int(i) for i in input().split()]
    n = len(arr)
    
    dp = [[1] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][i+1] = max(dp[i][i+1], dp[j][i]+1)
    
    return max(max(row) for row in dp)

print(longest_increasing_subsequence())
