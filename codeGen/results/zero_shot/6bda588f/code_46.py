import sys

def min_func_value(a, s):
    n = len(a)
    f_min = float('inf')
    
    for i in range(n):
        if a[i] > 2 * s:
            x_i = (a[i] - s) // 2
            y_i = a[i] - x_i
        else:
            x_i = max(0, a[i] - s)
            y_i = max(0, s - a[i])
        
        f_min = min(f_min, a[0] * x_i + y_i * a[1])
        
        for j in range(2, n):
            if a[j] > 2 * s:
                x_j = (a[j] - s) // 2
                y_j = a[j] - x_j
            else:
                x_j = max(0, a[j] - s)
                y_j = max(0, s - a[j])
            
            f_min = min(f_min, f_min + x_i * (a[j] - a[j-1]) + y_j * (a[j] - a[j-1]))
    
    return f_min

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_func_value(a, s))
