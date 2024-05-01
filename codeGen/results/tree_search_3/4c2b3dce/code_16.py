import sys

def contains_abba(s):
    n = len(s)
    # Create a suffix tree for the string
    stree = {}
    for i in range(n):
        curr = s[i:]
        for j in range(i+1, n+1):
            suffix = curr[:j]
            if suffix not in stree:
                stree[suffix] = 0
            stree[suffix] += 1

    # Search for 'AB' and 'BA' in the suffix tree
    ab_count = 0
    ba_count = 0
    for k, v in stree.items():
        if len(k) >= 2:
            if k[:2] == 'AB':
                ab_count += v
            elif k[:2] == 'BA':
                ba_count += v

    # Check if both patterns are present
    return ab_count > 0 and ba_count > 0

# Read the input string from standard input
s = sys.stdin.readline().strip()

# Print the result to standard output
print("YES" if contains_abba(s) else "NO")
