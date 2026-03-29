from collections import defaultdict

dp = defaultdict(int)

def min_operations(n, x):
    if n < 2 or x >= 10**(n-1):
        return -1
    if n == len(str(x)):
        return 0
    
    for k in range(1, n+1):
        last_digit = int((x / 10**(k-1)) % 10)
        if last_digit == 0:
            dp[(n-1, k+1)] = dp.get((n-1, k+1), 0) + 1
        else:
            dp[(n, k+1)] = dp.get((n, k+1), 0)
    
    return min_operations(n, x)

x, n = map(int, input().split())
print(min_operations(n, x))
