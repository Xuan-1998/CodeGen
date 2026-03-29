import sys
from collections import defaultdict

def can_partition(A, K, M):
    A.sort()
    max_val = max(A)
    min_val = min(A)

    # Check if there is no way to partition the array
    if max_val - min_val > M:
        return False

    partition_count = 0
    current_sum = 0
    partitions = defaultdict(int)

    for x in A:
        if x <= 0: continue
        if x + current_sum > M:
            current_sum = x
            partition_count += 1
            if partition_count >= K:
                return False
        else:
            current_sum += x

    return True


# Read input from standard input
N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

print(can_partition(A, K, M))
