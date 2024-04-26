import sys

def min_operations_to_beautiful(s, l, r):
    # Define the pattern to use for comparison
    pattern = "abc" * ((r - l + 1) // 3 + 1)
    # Initialize the count of operations
    operations = 0
    # Iterate over the substring and compare with the pattern
    for i in range(l, r):
        if s[i] != pattern[i - l]:
            operations += 1
    return operations

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Process each query
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    # Adjust the indices to be zero-based
    l -= 1
    r -= 1
    # Output the result for the current query
    print(min_operations_to_beautiful(s, l, r))
