import sys

def can_partition(A):
    N = len(A)
    K = int(sys.stdin.readline())
    
    # Validate K
    if K > N:
        return False
    
    A.sort()
    
    # Find the first possible partition
    for i in range(K-1, -1, -1):
        if A[i] + M < A[-1]:
            break
    else:
        return True
    
    # Check if the array can be further partitioned
    last = A[i]
    for j in range(i-1, -1, -1):
        if abs(A[j]-last) > M:
            return False
        last = A[j]
    
    return True

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.read().split()))
print(can_partition(A))
