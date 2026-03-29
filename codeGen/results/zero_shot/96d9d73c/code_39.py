import sys

def can_partition(A):
    A.sort()
    for i in range(len(A) - K + 1):
        max_val = A[i + K - 1]
        min_val = A[i]
        if max_val - min_val > M:
            return False
    return True

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(A))
