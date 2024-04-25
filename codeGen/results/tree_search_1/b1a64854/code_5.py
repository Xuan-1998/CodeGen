import sys

def min_sum_of_matrix(N, M):
    # Since the matrix is binary, the minimum sum is achieved when
    # each row and column has the same number of 1s, which is the
    # smaller of the two dimensions.
    return min(N, M) ** 2

# Read the number of test cases from standard input
T = int(input().strip())

# Iterate over each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().strip().split())
    
    # Calculate and print the minimum sum for the current test case
    print(min_sum_of_matrix(N, M))
