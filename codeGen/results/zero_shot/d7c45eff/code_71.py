import sys

def find_smallest_string(n, k, s):
    if k >= n:
        return s * (k // n) + s[:k % n]
    else:
        # Check if deleting the last character makes the string smaller
        if s[-1] < s[k - 1]:
            return s[:-1]
        else:
            return s

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
print(find_smallest_string(n, k, s))
