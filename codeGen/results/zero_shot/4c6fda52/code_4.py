import sys

def min_changes(s, k):
    n = len(s)
    r_count = g_count = b_count = 0
    
    # Count occurrences of each character
    for c in s:
        if c == 'R':
            r_count += 1
        elif c == 'G':
            g_count += 1
        else:
            b_count += 1
    
    # Calculate minimum occurrences required for a substring of length k
    min_occurrences = max(r_count // (k // 3), g_count // (k // 3), b_count // (k // 3)) * (k // 3)
    
    # Calculate minimum number of changes required
    changes_required = max(0, min_occurrences - r_count, min_occurrences - g_count, min_occurrences - b_count)
    
    return changes_required

q = int(sys.stdin.readline())
for _ in range(q):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
