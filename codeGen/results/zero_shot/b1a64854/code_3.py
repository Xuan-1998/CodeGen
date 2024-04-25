def min_sum_binary_matrix(T, test_cases):
    results = []
    for N, M in test_cases:
        if N != M:
            results.append(-1)  # No solution if N and M are different
        else:
            results.append(N)  # The minimum sum is N (or M) if N == M
    return results

# Read input from stdin
T = int(input().strip())
test_cases = []
for _ in range(T):
    N, M = map(int, input().strip().split())
    test_cases.append((N, M))

# Get the results
results = min_sum_binary_matrix(T, test_cases)

# Print the results to stdout
for result in results:
    print(result)
