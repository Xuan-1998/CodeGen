import sys

def is_possible_to_partition():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Sort the array in ascending order
    A.sort()

    # Initialize a counter for the number of partitions
    partition_count = 1

    # Initialize the minimum and maximum values for the current partition
    min_val = A[0]
    max_val = A[0]

    for i in range(1, N):
        if A[i] - max_val > M:
            # Start a new partition when the difference exceeds M
            partition_count += 1
            min_val = A[i]
            max_val = A[i]

    return partition_count >= K

print(is_possible_to_partition())
