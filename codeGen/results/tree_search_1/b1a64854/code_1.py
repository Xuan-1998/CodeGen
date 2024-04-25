import sys

def min_sum_binary_matrix(N, M):
    # The minimum sum is achieved by creating a square of '1's
    # with the size of the smaller dimension.
    return min(N, M)

# Read the number of test cases
T = int(sys.stdin.readline().strip())

# Process each test case
for _ in range(T):
    # Read N and M
    N, M = map(int, sys.stdin.readline().split())
    
    # Compute and print the result
    print(min_sum_binary_matrix(N, M))
