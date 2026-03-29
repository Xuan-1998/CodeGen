import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    # Initialize minimum F value to infinity
    min_f = float('inf')
    
    for x1 in range(s + 1):
        y1 = a[0] - x1
        for x2 in range(s + 1):
            y2 = a[1] - x2
            f = x1 * y2
            for i in range(2, n):
                x3 = min(x2, s) if y2 > 0 else max(x2, s)
                y3 = a[i] - x3
                f += x3 * y3
            min_f = min(min_f, f)
    
    print(min_f)
