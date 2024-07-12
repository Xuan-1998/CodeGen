python
def contains_non_overlapping_subsequences(s):
    n = len(s)
    found_AB = False
    found_BA = False

    for i in range(n - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 1  # Move to the next pair to avoid overlap
        elif s[i] == 'B' and s[i + 1] == 'A':
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 1  # Move to the next pair to avoid overlap

    print("NO")

# Read input from stdin
import sys
input = sys.stdin.read().strip()
contains_non_overlapping_subsequences(input)

