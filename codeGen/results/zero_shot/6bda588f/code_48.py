import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Initialize the minimum value of F
    min_f = float('inf')
    
    # Iterate over all possible values of x_i and y_i
    for i in range(n - 1):
        for j in range(a[i] + 1):
            if (j - s) * (a[i] - j) >= 0:
                f = a[0]
                for k in range(1, n):
                    f += (a[k] - j) * (k == i)
                min_f = min(min_f, f)
    
    print(min_f)
