def max_sum_after_partitioning(arr, k):
    n = len(arr)
    
    # Initialize a dictionary to store the maximum sum for each partition size
    dp = {1: [arr[0]]}
    
    for i in range(1, n):
        for j in range(min(i+1, k), 0, -1):
            if not dp.get(j):  # If there's no solution for this partition size yet
                continue
            
            # Calculate the maximum sum for the current partition size
            curr_max_sum = max(dp[j][-1], arr[i])
            
            # Update the maximum sum in the dictionary
            if j-1 not in dp:
                dp[j-1] = []
            dp[j-1].append(curr_max_sum)
    
    return sum(max(x) for x in dp.get(k, []))

# Read input from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(max_sum_after_partitioning(arr, k))
