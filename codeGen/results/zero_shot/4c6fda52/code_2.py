def min_changes(s, k):
    # Initialize the counter for character changes
    changes = 0
    
    # Iterate over all possible substrings of length k in s
    for i in range(len(s) - k + 1):
        window = s[i:i+k]
        
        # Check if the substring matches the first k-1 characters of the infinite string
        if window[:k-1] != "RGB" * (k-1 // 3):
            changes += 1
    
    return changes

# Read input from stdin
n, k = map(int, input().split())
s = input()

# Print the answer to stdout
print(min_changes(s, k))
