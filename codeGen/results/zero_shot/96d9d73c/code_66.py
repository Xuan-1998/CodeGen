import sys

def is_possible_to_partition(A, K, M):
    n = len(A)
    
    # If N < K, it's impossible to partition.
    if n < K:
        return False
    
    A.sort()
    
    # Initialize the current window's start and end indices.
    left = 0
    right = 0
    
    while right < n:
        # As long as we can fit at least K elements in the current window,
        # keep expanding it.
        while right - left >= K and A[right] - A[left] <= M:
            right += 1
        
        # If we've reached the end of the array, we're done!
        if right == n:
            return True
        
        # Otherwise, slide the window to the right and reset the count.
        left = right
        right += 1
    
    return False

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
print(is_possible_to_partition(A, K, M))
