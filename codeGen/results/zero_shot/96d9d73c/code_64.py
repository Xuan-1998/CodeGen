import sys

def is_possible_partition(A, K, M):
    N = len(A)
    A.sort()
    
    for i in range(N - K + 1):
        prev = A[i]
        for j in range(i + 1, min(i + K, N)):
            if abs(A[j] - prev) > M:
                return False
            prev = A[j]
    
    return True

N, K, M = map(int, sys.stdin.readline().split())
A = [int(x) for x in sys.stdin.readline().split()]
print(is_possible_partition(A, K, M))
