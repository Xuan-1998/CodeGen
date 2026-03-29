import sys

def min_function_value():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        
        # Calculate the minimum possible value of F
        f_min = 0
        for i in range(1, n):
            x_i = (a[i] - s) // 2
            y_i = a[i] - s - 2 * x_i
            f_min += x_i * a[i-1] + y_i * a[i]
        
        print(f_min)

min_function_value()
