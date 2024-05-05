import sys

n, k, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

partition_sum = 0
num_partitions = 0

for i in range(n):
    if A[i] - partition_sum >= m:  # Check if we can start a new partition
        num_partitions += 1
        partition_sum = A[i]
    else:
        partition_sum += A[i]

if num_partitions + 1 < k:  # Check if we have at least K partitions
    print(False)
else:
    print(True)
