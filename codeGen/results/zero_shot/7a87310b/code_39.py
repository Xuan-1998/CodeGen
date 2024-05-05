import sys

def generate_matrices_with_trace_n(n):
    # Initialize count to 0
    count = 0
    
    for a in range(-n//2 + 1, n//2 + 1):
        for b in range(-n//2 + 1, n//2 + 1):
            if abs(a) + abs(b) == n:  # Check if the trace is N
                for c in range(-1000, 1001):  # Iterate over possible middle element values
                    d = n - a - c  # Calculate the bottom-right element value
                    det = (a * d) - (b * c)
                    if det > 0:  # Check if the determinant is positive
                        count += 1
    
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    result = generate_matrices_with_trace_n(N)
    print(result)
