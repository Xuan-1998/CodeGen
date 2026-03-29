import sys

def find_min_value():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().strip().split())
        
        a = list(map(int, sys.stdin.readline().strip().split()))
        
        min_value = 0
        
        for i in range(1, n-1):
            x = min(s, a[i])
            y = max(0, a[i] - s)
            
            if i < n - 2:
                min_value += (x - s) * (y - s)
            else:
                min_value += x * y
        
        print(min_value)

if __name__ == "__main__":
    find_min_value()
