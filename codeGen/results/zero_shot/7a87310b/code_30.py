import itertools

def count_matrices(N):
    matrices = []
    for a in range(1, N+1):  # Generate all possible a
        for b in range(a+1, N+1):  # Ensure determinant > 0
            for c in range(b+1, N+1):  # Ensure determinant > 0
                d = (a * c) - (b * b)
                if d > 0:  # Check determinant is positive
                    matrices.append([[a, b], [c, d]])
    return len(matrices)

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
