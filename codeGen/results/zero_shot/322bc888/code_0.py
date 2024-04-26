def min_operations_to_beautiful(s, queries):
    # Function to find the next different character
    def next_diff_char(c):
        for char in 'abc':
            if char != c:
                return char
        return None

    results = []
    for l, r in queries:
        # Extract the substring for the current query
        substring = s[l-1:r]
        operations = 0

        # Iterate over the substring and apply the rules
        i = 0
        while i < len(substring) - 1:
            if substring[i] == substring[i+1]:
                # If two consecutive characters are the same, change the second one
                next_char = next_diff_char(substring[i])
                substring = substring[:i+1] + next_char + substring[i+2:]
                operations += 1
            if i < len(substring) - 2 and substring[i] == substring[i+2]:
                # If a character is the same as the one two positions ahead, change the middle one
                next_char = next_diff_char(substring[i+1])
                substring = substring[:i+1] + next_char + substring[i+2:]
                operations += 1
            i += 1

        results.append(operations)
    
    return results

# Read the input
n, m = map(int, input().split())
s = input()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print the results for each query
results = min_operations_to_beautiful(s, queries)
for res in results:
    print(res)
