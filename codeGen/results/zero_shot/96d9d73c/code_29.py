import sys

def can_partition(A):
    N = len(A)
    A.sort()

    partitions = []
    current_partition = [A[0]]
    max_value = A[0]
    for i in range(1, N):
        if A[i] - max_value > M or len(current_partition) < K:
            partitions.append(current_partition[:])
            current_partition = [A[i]]
            max_value = A[i]
        else:
            current_partition.append(A[i])
            max_value = max(max_value, A[i])

    partitions.append(current_partition)
    return any(len(partition) >= K for partition in partitions)

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.read().strip().split()))
print(can_partition(A))
