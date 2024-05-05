import sys

def count_matrices(N):
    # Initialize the count to 0
    count = 0
    
    for a in range(1, N // 2 + 1):
        for b in range(a, N // 2 + 1):
            c = (N - a) // (b - a)
            d = N - a - c * (b - a)
            
            if d > 0 and is_invertible(a, b, c, d):
                count += 1
    
    return count

def is_invertible(a, b, c, d):
    # Calculate the determinant
    det = a * d - b * c
    
    # Check if the determinant is positive and the matrix is invertible
    return det > 0 and (a * d != b * c)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_matrices(N))
