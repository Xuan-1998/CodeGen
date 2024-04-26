def min_operations_to_beautiful(s, queries):
    results = []
    for l, r in queries:
        # Extract the substring for the current query
        substring = s[l-1:r]
        # Initialize the number of operations
        operations = 0
        
        # Iterate through the substring to find and break palindromes
        for i in range(1, len(substring)):
            # If two consecutive characters are the same, we need an operation
            if substring[i] == substring[i-1]:
                operations += 1
                # Change the current character to the next character in 'abc'
                next_char = 'abc'[('abc'.index(substring[i-1]) + 1) % 3]
                # Create a new substring with the changed character
                substring = substring[:i] + next_char + substring[i+1:]
        
        results.append(operations)
    
    return results

# Read input from stdin
n, m = map(int, input().split())
s = input()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate the number of operations for each query
results = min_operations_to_beautiful(s, queries)

# Print the results to stdout
for result in results:
    print(result)
