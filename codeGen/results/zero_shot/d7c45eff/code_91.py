import sys

def smallest_string(k, s):
    if k >= len(s):
        return s[:k]

    if k <= len(s) // 2:
        return s + s[:len(s)-1]
    else:
        return s[:-1]

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

print(smallest_string(k, s))
