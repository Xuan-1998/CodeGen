def min_sum_binary_matrix(N, M):
    # The minimum sum of the binary matrix is the smaller of the two dimensions
    return min(N, M)

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N, M = map(int, input().split())
    result = min_sum_binary_matrix(N, M)
    print(result)
