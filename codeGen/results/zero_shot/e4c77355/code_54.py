def longest_increasing_subsequence():
    # Read input from stdin
    arr = [int(x) for x in input().split()]
    
    n = len(arr)
    dp = [1] * n  # Initialize the table with ones
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

print(longest_increasing_subsequence())
