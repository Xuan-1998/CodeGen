def min_operations_to_beautiful_substring(n, m, s, queries):
    results = []
    for query in queries:
        l, r = query
        # We'll use the modulo operator to alternate between 'a', 'b', and 'c'
        expected_chars = ['a', 'b', 'c']
        cost = 0
        for i in range(l - 1, r):
            # Check if the current character is what we expect it to be
            if s[i] != expected_chars[(i - l + 1) % 3]:
                cost += 1
        results.append(cost)
    return results

# Read input from stdin
n, m = map(int, input().split())
s = input()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Get the results for all queries
results = min_operations_to_beautiful_substring(n, m, s, queries)

# Print the results to stdout
for result in results:
    print(result)
