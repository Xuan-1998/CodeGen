def min_sum_binary_matrix(T, test_cases):
    for N, M in test_cases:
        min_sum = min(N, M)
        print(min_sum)

# Read input from stdin
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

min_sum_binary_matrix(T, test_cases)
