import sys

def is_possible_partition(A, K, M):
    A.sort()
    last_seen = A[0]
    partition_count = 1
    for num in A:
        if num > last_seen + M:
            last_seen = num
            partition_count += 1
        if partition_count >= K:
            return True
    return False

# Read input from stdin
N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.read().split()))

# Check if it's possible to partition the array
if is_possible_partition(A, K, M):
    print("True")
else:
    print("False")
