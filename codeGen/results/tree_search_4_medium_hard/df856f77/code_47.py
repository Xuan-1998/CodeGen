def min_operations(array):
    n = len(array)
    dp = [0] * (n + 1)
    
    # Base case: A[0] is always in its correct position, so dp[0] is 0.
    for i in range(1, n):
        if array[i] > array[i - 1]:
            # If Ai > Ai+1, then the minimum number of operations needed to make
            # the subarray A[0..i] strictly increasing is dp[i-1] + 1.
            dp[i] = dp[i - 1] + 1
        else:
            # Otherwise, dp[i] can take the value of either dp[i-1] or dp[i-2],
            # depending on whether Ai+1 is greater than any previous element in A.
            dp[i] = min(dp[i - 1], dp[i - 2]) + (1 if array[i] > max(array[:i - 1]) else 0)
    
    return dp[-1]

# Read input
n, *array = map(int, input().split())

print(min_operations(array))
