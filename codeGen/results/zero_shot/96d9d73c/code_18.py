import sys

def can_partition(A):
    N = len(A)
    A.sort()
    
    for i in range(N - K + 1):
        prev = A[i]
        for j in range(i + K, N):
            if abs(A[j] - prev) > M:
                return False
            prev = A[j]
    
    return True

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

print(can_partition(A))
