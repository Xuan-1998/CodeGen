import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

def min_operations_to_beautify(s, l, r):
    # We'll only need to change characters at even indices (0-based)
    # to avoid palindromes of length 2 or 3.
    operations = 0
    for i in range(l, r):
        # Check if we're at an even index and if the next two characters are the same.
        # Or if the next three characters form a palindrome.
        if (i - l) % 2 == 0:
            if i + 1 < r and s[i] == s[i + 1]:
                operations += 1
            elif i + 2 < r and s[i] == s[i + 2]:
                operations += 1
    return operations

# Process queries
for l, r in queries:
    # Adjust indices to be 0-based
    l -= 1
    r -= 1
    print(min_operations_to_beautify(s, l, r))
