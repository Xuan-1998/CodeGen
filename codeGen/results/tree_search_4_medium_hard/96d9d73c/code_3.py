def canPartition(A):
    N, K, M = len(A), 0, 0
    A.sort()
    
    for i in range(N):
        if A[i] <= M:
            M = A[i]
        else:
            break

    for i in range(N-1, -1, -1):
        if A[i] - M <= A[0]:
            return True
        else:
            return False

# example usage
N, K, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

print(canPartition(A))
