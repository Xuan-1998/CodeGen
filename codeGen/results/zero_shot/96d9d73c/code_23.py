import sys

def can_partition(n, k, m, A):
    A.sort()
    
    left = 0
    right = n - 1
    
    while left < right:
        if A[right] - A[left] <= m:
            left += 1
        else:
            right -= 1
            
    return (right + 1) >= k

n, k, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
print(can_partition(n, k, m, A))
