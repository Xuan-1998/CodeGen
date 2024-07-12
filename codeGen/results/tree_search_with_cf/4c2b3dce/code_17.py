python
def contains_non_overlapping_subsequences(s):
    n = len(s)
    if n < 2:
        print("NO")
        return

    found_AB = False
    found_BA = False

    i = 0
    while i < n - 1:
        if s[i:i+2] == "AB":
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 2  # Skip the next character to avoid overlap
        elif s[i:i+2] == "BA":
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 2  # Skip the next character to avoid overlap
        else:
            i += 1

    print("NO")

# Reading input from stdin
import sys
input = sys.stdin.read().strip()
contains_non_overlapping_subsequences(input)

