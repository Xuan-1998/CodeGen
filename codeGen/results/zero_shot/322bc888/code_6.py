def min_operations_to_beautiful(s, queries):
    results = []
    for l, r in queries:
        # Extract the substring for the current query
        substring = s[l-1:r]
        # Initialize the number of operations
        operations = 0
        # Iterate through the substring to count the operations needed
        for i in range(1, len(substring)):
            # If the current character is the same as the previous one,
            # we need to change it.
            if substring[i] == substring[i-1]:
                operations += 1
                # To avoid creating a palindrome of length 3, we change the character
                # to one that is not the same as the character two positions before.
                if i + 1 < len(substring):
                    next_char = 'a' if substring[i+1] == 'b' or (i > 1 and substring[i-2] == 'b') else 'b'
                    substring = substring[:i] + next_char + substring[i+1:]
        results.append(operations)
    return results

# Read input from stdin
n, m = map(int, input().split())
s = input().strip()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Get the results for each query
results = min_operations_to_beautiful(s, queries)

# Print the results to stdout
for result in results:
    print(result)
