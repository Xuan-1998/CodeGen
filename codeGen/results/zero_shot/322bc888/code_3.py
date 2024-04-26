def is_palindrome(s):
    return s == s[::-1]

def min_operations(s, queries):
    results = []
    for l, r in queries:
        # Extract the substring
        substring = s[l-1:r]
        
        # Check for palindromes and count operations
        operations = 0
        for i in range(1, len(substring)):
            if substring[i] == substring[i-1]:
                operations += 1
                break  # Only one change needed to break the palindrome

        # Append the result for the current query
        results.append(operations)
    return results

# Read input from stdin
n, m = map(int, input().split())
s = input().strip()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result for each query
results = min_operations(s, queries)

# Print the results to stdout
for res in results:
    print(res)
