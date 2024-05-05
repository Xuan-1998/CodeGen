import sys

def solve():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().strip().split())
        
        a = list(map(int, sys.stdin.readline().strip().split()))
        
        min_f = float('inf')
        
        for i in range(n - 1):
            x = min(s, a[i])
            y = a[i] - x
            
            f = x * (a[i + 1] - s) + y * (y + s)
            
            if f < min_f:
                min_f = f
        
        print(min_f)

if __name__ == "__main__":
    solve()
