def min_sum_of_binary_matrix(N, M):
    # The minimum sum is the square of the smaller dimension
    # because that's the maximum number of 1s we can have
    # such that each row and column has the same sum.
    return min(N, M) ** 2

# Read the number of test cases
T = int(input())
# Iterate over each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().split())
    # Calculate and print the minimum sum for the current test case
    print(min_sum_of_binary_matrix(N, M))
