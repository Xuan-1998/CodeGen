import sys
from math import comb

def solve():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        
        p1 = []
        p2 = []
        
        for _ in range(n):
            a, b, proba = map(float, sys.stdin.readline().split())
            
            if not p1:
                p1.append((0.0, 0))
                p2.append((0.0, 0))
            
            p1.append((proba, 0))
            p2.append((proba, a))
        
        ans = 1
        
        for x, y in zip(p1, p2):
            if len(set([x[1], y[1]])) == n:
                ans *= x[0]
            else:
                ans *= (x[0] * comb(n-1, n-x[1]-y[1]) / comb(n, x[1]+y[1]))
        
        print('%.6f' % ans)

if __name__ == "__main__":
    solve()
