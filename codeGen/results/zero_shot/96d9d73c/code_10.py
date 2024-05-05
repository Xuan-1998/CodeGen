def can_partition(N, K, M, A):
    A.sort()
    
    left = 0
    right = 0
    
    while right < N:
        if A[right] - A[left] > M:
            return False
        
        right += 1
        if right >= K:
            left = right
            right += 1
            
    return True

# Read input from stdin and print the result to stdout
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

print(can_partition(N, K, M, A))
