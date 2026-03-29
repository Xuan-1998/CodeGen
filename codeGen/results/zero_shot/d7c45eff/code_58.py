import sys

def find_smallest_string(n, k, s):
    if n <= k:
        return s[:k]
    
    # If the length of the original string is greater than or equal to k,
    # then we need to either delete the last character or duplicate the string.
    if k % 2 == 0:  # If k is even, it's more efficient to duplicate the string
        return s * (k // 2)
    else:
        # If k is odd, we can either duplicate the first part of the string and delete the last character,
        # or keep the original string intact.
        if n > k:  # Keep the original string intact
            return s[:k]
        else:
            return s

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

print(find_smallest_string(n, k, s))
