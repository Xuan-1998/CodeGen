import sys

def is_partition_possible(N, K, M, A):
    # Sort the array
    A.sort()

    # Check if we can partition the array into at least K partitions
    for i in range(K - 1):
        if A[i + 1] - A[i] > M:
            return False

    # Check if the last partition has at least K elements
    if len(A) % K != 0 or A[-1] - A[0] > M:
        return False

    return True


N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if is_partition_possible(N, K, M, A):
    print("True")
else:
    print("False")
