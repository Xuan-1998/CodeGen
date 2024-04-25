import sys

def min_sum_binary_matrix(N, M):
    # The minimum sum is achieved by filling a square submatrix of size min(N, M)
    # with 1s because that's the largest square that fits into the N x M matrix.
    return min(N, M)**2

# Read the number of test cases
T = int(sys.stdin.readline().strip())

# Process each test case
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    result = min_sum_binary_matrix(N, M)
    print(result)
