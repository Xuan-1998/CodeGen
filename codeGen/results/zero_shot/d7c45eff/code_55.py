import sys

n, k = map(int, input().split())
s = input().strip()

def solve():
    if len(s) <= k:
        return s[:k]
    else:
        if k % 2 == 0:
            return s[:k//2] + s[:k//2]
        else:
            return s[:k//2] + s[k//2]

print(solve())
