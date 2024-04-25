def min_sum_binary_matrix(T, test_cases):
    results = []
    for N, M in test_cases:
        # The minimum sum is equal to the smaller of the two dimensions.
        results.append(min(N, M))
    return results

# Read input from stdin and output the answer to stdout
if __name__ == "__main__":
    T = int(input().strip())
    test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
    results = min_sum_binary_matrix(T, test_cases)
    for result in results:
        print(result)
