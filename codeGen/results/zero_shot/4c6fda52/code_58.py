def min_changes(s, k):
    R_count = s[:k-1].count('R')
    G_count = s[:k-1].count('G')
    B_count = s[:k-1].count('B')

    return max(R_count, G_count, B_count)

# Read input from stdin
n, k = map(int, input().split())
s = input()

# Calculate the minimum number of changes
min_changes_needed = min_changes(s, k)

# Print the answer to stdout
print(min_changes_needed)
