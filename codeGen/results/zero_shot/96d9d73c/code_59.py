import sys

def can_partition(A, K, M):
    A.sort()
    last = 0
    for i in range(len(A)):
        if A[i] - A[last] > M:
            last = i
            if i + 1 < len(A) and A[i + 1] - A[i] > M:
                return False
    if len(A) // K * K != len(A):
        return False
    return True

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
print(can_partition(A, K, M))
