from collections import defaultdict

def count_invertible_matrices():
    T = int(input())  # Read number of test cases from stdin
    memo = defaultdict(int)  # Initialize memoization dictionary

    for _ in range(T):
        N = int(input())  # Read trace value from stdin
        count = 0

        for a in range(1, N + 1):
            for b in range(N - a + 1):
                if (a - b) * 2 > 0 and abs(a - b) < N:
                    t = a + b
                    sign = 1 if (a - b) > 0 else -1

                    # Check if the matrix has positive determinant
                    if (a * sign) * ((N - a) * sign) > 0:
                        count += 1

        print(count)  # Print the count of invertible matrices with positive determinant and trace N

count_invertible_matrices()
