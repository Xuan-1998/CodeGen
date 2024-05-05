def min_changes_to_match(s, k):
    # Find all occurrences of the substring k in s
    matches = [i for i in range(len(s) - k + 1) if s[i:i+k] == 'RGB' * (k // 3)]
    
    # Count the number of characters that need to be changed
    changes = len(s) - sum(1 for match in matches)
    
    return changes

# Read input from stdin
n, k = map(int, input().split())
s = input().strip()

# Calculate the minimum number of characters that need to be changed
min_changes = min_changes_to_match(s, k)

# Print the result to stdout
print(min_changes)
