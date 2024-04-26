import sys

def min_operations_to_make_beautiful(s, queries):
    results = []
    for l, r in queries:
        operations = 0
        i = l - 1
        while i < r - 1:  # -1 because string indices are 0-based
            if s[i] == s[i + 1]:  # Check for palindrome of length 2
                operations += 1
                i += 2  # Skip the next character
            elif i < r - 2 and s[i] == s[i + 2]:  # Check for palindrome of length 3
                operations += 1
                i += 3  # Skip the next two characters
            else:
                i += 1
        results.append(operations)
    return results

# Read input from stdin
n, m = map(int, sys.stdin.readline().strip().split())
s = sys.stdin.readline().strip()
queries = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

# Get the results
results = min_operations_to_make_beautiful(s, queries)

# Print results to stdout
for res in results:
    print(res)
