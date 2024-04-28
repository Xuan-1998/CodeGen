def max_partitions(arr):
    n = len(arr)
    total_sum = sum(arr)
    
    # Create a 1D array dp with size (total_sum / 2 + 1) to store the maximum number of times the array can be partitioned up to the current position.
    dp = [0] * ((total_sum // 2) + 1)
    
    for i in range(n):
        for j in range(total_sum // 2, arr[i] - 1, -1):
            if j - arr[i] >= 0:
                dp[j] = max(dp[j], dp[j - arr[i]] + 1)
    
    # Find the maximum number of times the array can be partitioned.
    for i in range((total_sum // 2) + 1):
        if total_sum - 2 * i >= 0 and dp[total_sum - 2 * i] > 0:
            return dp[total_sum - 2 * i]
    
    # If no partitions are found, return 0.
    return 0

# Read input from standard input.
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(max_partitions(arr))
