def min_sum_for_binary_matrix(N, M):
    # If the matrix is square, fill it with 1s, else with 0s
    return N * M if N == M else 0

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().split())
    # Output the minimum sum for the current test case
    print(min_sum_for_binary_matrix(N, M))
