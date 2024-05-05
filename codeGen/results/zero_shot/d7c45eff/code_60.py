import sys

def smallest_string(n, k, s):
    if n == k:
        return s
    
    if k <= len(s) // 2:
        return s[:k]
    
    return s[:k-1] if s[k-1] <= s[0] else s[:1]

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

print(smallest_string(n, k, s))
