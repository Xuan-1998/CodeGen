import sys

def solve(n, k, s):
    # Delete the last character of the original string
    if n > k:
        s = s[:-1]
    else:
        # Duplicate the original string to match length k
        s = s * (k // n + 1)
        s = s[:k]

    return s

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(solve(n, k, s))
