import sys

def min_changes(s, k):
    changes = 0
    for i in range(k-1):
        if s[i] != 'R' and s[i] != 'G':
            changes += 1
    return changes

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Calculate the minimum number of changes needed
changes = min_changes(s, k)

# Print the answer to stdout
print(changes)
