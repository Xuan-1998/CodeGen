import sys

def min_f(a):
    n = len(a)
    a.sort()
    res = 0
    s = sum(a)
    
    for i in range(n-1):
        x = a[i]
        y = s - x
        res += x * y
    
    return res

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    print(min_f(a))
