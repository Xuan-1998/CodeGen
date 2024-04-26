def find_patterns(s, pattern1, pattern2):
    # Find the first pattern
    pos1 = s.find(pattern1)
    if pos1 != -1:
        # If found, start searching for the second pattern after the first
        pos2 = s.find(pattern2, pos1 + 2)
        if pos2 != -1:
            return True
    # Repeat the process with reversed patterns to cover both orders
    pos1 = s.find(pattern2)
    if pos1 != -1:
        pos2 = s.find(pattern1, pos1 + 2)
        if pos2 != -1:
            return True
    return False

# Read input from stdin
s = input().strip()

# Check if both patterns "AB" and "BA" are present
if find_patterns(s, "AB", "BA"):
    print("YES")
else:
    print("NO")
