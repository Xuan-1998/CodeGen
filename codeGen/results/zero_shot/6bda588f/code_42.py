import sys

def min_function_value():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        # Initialize the minimum value of F
        min_f = float('inf')
        
        # Iterate over all possible values of x_i and y_i
        for i in range(n):
            x = a[i] - s
            if x < 0:
                break
            for j in range(i+1, n):
                y = a[j] - s
                if y < 0:
                    break
                f = sum(x * (a[k] - s) for k in range(i, j+1))
                min_f = min(min_f, f)
        
        print(min_f)

min_function_value()
