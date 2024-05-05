import sys

def can_partition(A, K, M):
    # Sort the array in ascending order
    A.sort()

    # Initialize the count of partitions
    count = 1

    # Initialize the current partition sum and minimum value
    total_sum = A[0]
    min_val = A[0]

    for i in range(1, len(A)):
        # If the current element is more than M away from the previous one,
        # we need to start a new partition
        if abs(A[i] - min_val) > M:
            count += 1
            total_sum = A[i]
            min_val = A[i]
        else:
            total_sum += A[i]
            min_val = min(min_val, A[i])

    return count >= K

# Read input from stdin
N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# Print the output to stdout
print(can_partition(A, K, M))
