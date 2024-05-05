import sys

def solve(a, s):
    n = len(a)
    min_f = float('inf')
    
    for x in range(s + 1):
        y = a[0] - x
        f = x * (y - s) if x > s else 0
        for i in range(1, n):
            x += y
            y = a[i] - x
            f += x * (y - s) if x > s else 0
        min_f = min(min_f, f)
    
    return min_f

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, s))
