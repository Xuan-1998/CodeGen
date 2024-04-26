import sys

def min_operations_to_beautiful(s, l, r):
    operations = 0
    # We need to check two and three character groups.
    # We start from l - 1 because the string is 1-indexed in the problem statement.
    i = l - 1
    while i < r:
        # Check for a palindrome of length 2.
        if i < r - 1 and s[i] == s[i + 1]:
            operations += 1
            i += 2  # Skip the next character because we've already changed it.
        # Check for a palindrome of length 3.
        elif i < r - 2 and s[i] == s[i + 2]:
            operations += 1
            i += 3  # Skip the next two characters because we've already changed one.
        else:
            i += 1
    return operations

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    print(min_operations_to_beautiful(s, l, r))
