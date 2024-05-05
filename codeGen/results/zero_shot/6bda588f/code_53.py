import sys

def calculate_min_f(a, s):
    n = len(a)
    min_f = float('inf')
    
    for i in range(n-1):
        x = (a[i] - s) if a[i] >= s else 0
        y = a[i] - x
        temp_sum = 0
        
        for j in range(i+1, n-1):
            temp_x = (a[j] - s) if a[j] >= s else 0
            temp_y = a[j] - temp_x
            temp_sum += min(x*a[j], y*temp_x)
            x, y = temp_x, temp_y
        
        temp_sum += a[-1]*s if a[-1] > s else 0
        min_f = min(min_f, temp_sum)
    
    return min_f

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(calculate_min_f(a, s))
