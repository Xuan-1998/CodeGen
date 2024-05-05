import sys

def solve(n, k, s):
    # Count the frequency of each character
    freq = {'R': 0, 'G': 0, 'B': 0}
    for c in s:
        freq[c] += 1
    
    # Calculate the minimum number of changes needed
    min_changes = 0
    for c, count in freq.items():
        if count % k > 0:  # need to change some characters
            min_changes += (count + k - 1) // k * 3  # add extra 'R', 'G', and 'B' to make up the remainder
    
    return min_changes

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Print the answer to stdout
print(solve(n, k, s))
