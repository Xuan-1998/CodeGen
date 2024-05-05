import sys

def is_possible_partitioning(n, k, m, A):
    max_val = max(A)
    min_val = min(A)

    if abs(max_val - min_val) > m:
        return False

    current_partition_max = min_val
    for x in A:
        if x > current_partition_max + m:
            if len(A[:x]) < k:
                return False
            current_partition_max = x
    return True

n, k, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
print(is_possible_partitioning(n, k, m, A))
