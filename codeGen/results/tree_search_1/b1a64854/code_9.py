import sys

def min_sum_binary_matrix(N, M):
    # The minimum sum is the square of the smaller dimension.
    return min(N, M) ** 2

# Read the number of test cases.
T = int(sys.stdin.readline().strip())

# Process each test case.
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    result = min_sum_binary_matrix(N, M)
    print(result)
