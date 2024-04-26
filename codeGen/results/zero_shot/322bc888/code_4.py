def min_operations_to_beautiful(s, queries):
    results = []
    for l, r in queries:
        # Since the string only consists of 'a', 'b', 'c',
        # any three consecutive characters that are not the same
        # will not form a palindrome. Thus, we only need to check
        # every two consecutive characters.
        count = 0
        for i in range(l - 1, r - 1):
            if s[i] == s[i + 1]:
                count += 1
        results.append(count)
    return results

# Read input from stdin
n, m = map(int, input().split())
s = input().strip()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Get the results
results = min_operations_to_beautiful(s, queries)

# Print the results to stdout
for result in results:
    print(result)
