import sys

def solve(n, k, s):
    if n <= k:
        return s[:k] if k > 0 else ""

    # If the original string has a length greater than k,
    # we can simply truncate it to the desired length k.
    truncated_s = s[:-1] if k < n else s

    if k == n:
        return s
    elif k > n:
        return truncated_s
    else:  # k <= n
        if s[-1] <= sorted(s)[k-1]:
            return truncated_s[:k]
        else:
            return truncated_s + s[-1]

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

print(solve(n, k, s))
