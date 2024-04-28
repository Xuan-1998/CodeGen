def maxPartitionSumEqual(arr):
    n = len(arr)
    
    # Initialize the dp table
    dp = [0] * (n + 1)
    
    # Base case: for i = 0, we consider the whole array as a single partition
    total_sum = sum(arr)
    left_sum = 0
    
    # Calculate the base case value
    if total_sum % 2 == 0:
        dp[0] = 1
    else:
        dp[0] = 0
    
    # Fill up the dp table using bottom-up dynamic programming
    for i in range(1, n + 1):
        left_sum += arr[i - 1]
        
        if total_sum % 2 == 0:
            right_sum = total_sum - left_sum
            for j in range(i):
                # Calculate the maximum number of times array[0..j] can be partitioned into two contiguous subarrays with equal sum
                if dp[j] + (right_sum == left_sum) > dp[i]:
                    dp[i] = dp[j] + (right_sum == left_sum)
        else:
            for j in range(i):
                # Calculate the maximum number of times array[0..j] can be partitioned into two contiguous subarrays with equal sum
                if dp[j] > dp[i]:
                    dp[i] = dp[j]
    
    return dp[n]

# Read input from standard input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Calculate the maximum number of times array can be partitioned into two contiguous subarrays with equal sum
    print(maxPartitionSumEqual(arr))

