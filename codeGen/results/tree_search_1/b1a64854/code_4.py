import sys

def min_matrix_sum(N, M):
    # The minimum sum is achieved when we have a square submatrix of 1s
    # with side length equal to the minimum of N and M.
    return min(N, M)

# Read number of test cases from stdin
T = int(input().strip())

# Process each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().strip().split())
    # Output the minimum sum for the current test case
    print(min_matrix_sum(N, M))
