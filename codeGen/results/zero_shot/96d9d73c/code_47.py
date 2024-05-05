import sys

def can_partition(n, k, m, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the current partition and its minimum value
    curr_min = arr[0]
    curr_max = arr[0]
    curr_count = 1
    
    # Iterate through the array
    for i in range(1, n):
        # If the current element is more than M away from the previous maximum,
        # start a new partition
        if arr[i] - curr_max > m:
            curr_min = arr[i]
            curr_max = arr[i]
            curr_count = 1
        
        # Update the current partition's minimum and maximum values
        else:
            curr_min = min(curr_min, arr[i])
            curr_max = max(curr_max, arr[i])
            curr_count += 1
        
        # If we've reached or exceeded K elements in the current partition,
        # return True (partitioning is possible)
        if curr_count >= k:
            return True
    
    # If we reach the end of the array without meeting the condition,
    # return False (partitioning is not possible)
    return False

# Read input from stdin
n, k, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# Call the can_partition function and print the result to stdout
print(can_partition(n, k, m, arr))
