import sys

# Read input from stdin
N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# Sort the array A
A.sort()

# Initialize the partition count and the current partition size
partition_count = 0
current_partition_size = 0

# Iterate over the sorted array to find partitions
for i in range(N):
    # Add the current element to the current partition
    current_partition_size += 1
    
    # If we have reached the minimum partition size or this is the last element
    if current_partition_size >= K or i == N - 1:
        # Check if the absolute difference between the first and last elements in the current partition does not exceed M
        if i > 0 and A[i] - A[0] <= M:
            # Increment the partition count
            partition_count += 1
            
            # Reset the current partition size for the next iteration
            current_partition_size = 0
        else:
            # If we have found a partition that does not satisfy the conditions, break the loop
            break

# Print the answer to stdout
print(partition_count > 0)
