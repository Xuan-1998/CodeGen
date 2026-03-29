import sys

def solve(N, M, C):
    # Initialize the result array with zeros
    res = [0] * (C + 1)
    
    # Iterate over all possible radii from 1 to C
    for i in range(1, C+1):
        # Calculate the number of upper hemispheres with radius i
        up_hemi = sum(1 for j in range(N) if U_j <= i)
        
        # Calculate the number of lower hemispheres with radius i
        low_hemi = sum(1 for j in range(M) if L_j <= i)
        
        # Update the result array with the modulo 10^9+7 value
        res[i] = (res[i-1] + up_hemi * low_hemi) % (10**9+7)
    
    return ' '.join(map(str, res))

# Read input from stdin
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    
    print(solve(N, M, C))
