import sys

def solve(n, k):
    s = input().strip()
    
    if k <= n:
        if k == n:
            return s[:k]
        elif k < n:
            return min(s, s[:-1], key=len)
    else:
        # If k > n, we need to extend the string
        extended_s = ''
        for _ in range(k - n):
            extended_s += s
        if k % n == 0 and len(extended_s) < k:
            return min([s, extended_s], key=len)
        else:
            return extended_s

n, k = map(int, input().split())
print(solve(n, k))
