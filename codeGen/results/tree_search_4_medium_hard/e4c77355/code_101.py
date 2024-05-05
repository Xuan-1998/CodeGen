def find_LIS_length(arr):
    n = len(arr)
    
    # Initialize the dp table with all values set to 1
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read input from stdin
arr = list(map(int, input().split()))
print(find_LIS_length(arr))
