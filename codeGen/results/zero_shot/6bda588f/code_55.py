import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        min_f = float('inf')
        for i in range(n):
            if a[i] > s:
                x_i = a[i] - s
                y_i = 0
            else:
                x_i = s
                y_i = a[i]
            
            f = x_i * (a[1] - s) + y_i * (a[2] - s)
            min_f = min(min_f, f)
        
        print(min_f)

if __name__ == "__main__":
    solve()
