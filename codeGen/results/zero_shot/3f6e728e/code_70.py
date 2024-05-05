import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        U = list(map(int, sys.stdin.readline().split()))
        L = list(map(int, sys.stdin.readline().split()))
        
        # Sort radii in ascending order
        U.sort()
        L.sort()
        
        # Initialize the count of X-sequences for each size
        xseq_count = [0] * (C + 1)
        
        # Count the combinations of upper and lower hemispheres
        i, j = 0, 0
        while i < N or j < M:
            if U[i] >= L[j]:
                xseq_count[L[j]] += 1
                j += 1
            else:
                i += 1
        
        # Print the count of X-sequences for each size
        print(' '.join(map(str, xseq_count[:C])))

solve()
