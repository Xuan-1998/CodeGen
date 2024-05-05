import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        ans = float('inf')
        for i in range(n-1):
            x = min(a[i], s)
            y = a[i] - x
            if (a[i+1]-s)*(y-s) >= 0:
                f = a[i]*x + y*a[i+1]
                ans = min(ans, f)
        
        print(min(ans, a[-1]*min(a[-1], s)))
