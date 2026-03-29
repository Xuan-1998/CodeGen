import sys

def max_path_sum(arr):
    n = len(arr)
    
    # Initialize variables to store maximum sum and current sum
    max_sum = -1000 * 10 ** 3  # Arbitrarily set initial value as negative infinity
    curr_sum = 0
    
    for i in range(n):
        if arr[i] > 0:  # If the node has a positive value, consider it as part of the current sum
            curr_sum += arr[i]
        else:
            max_sum = max(max_sum, curr_sum)  # Update maximum sum if necessary
            curr_sum = 0
    
    return max(max_sum, curr_sum)

# Read input from stdin
arr = [int(x) for x in sys.stdin.read().split()]

# Print the output to stdout
print(max_path_sum(arr))
