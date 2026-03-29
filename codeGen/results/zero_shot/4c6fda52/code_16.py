import sys

def min_changes(s, k):
    # Initialize the changed count to 0
    changed_count = 0
    
    # Try to extend the substring from the left
    for i in range(k-1, -1, -1):
        if s[i:i+k] == "RGB" or s[i:i+k] == "BGR":
            break
        else:
            changed_count += 1
    
    # Try to extend the substring from the right
    for i in range(k-1, len(s)):
        if s[i-k+1:i+1] == "RGB" or s[i-k+1:i+1] == "BGR":
            break
        else:
            changed_count += 1
    
    return changed_count

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Calculate the minimum number of changes
changed_count = min_changes(s, k)

# Print the answer to stdout
print(changed_count)
