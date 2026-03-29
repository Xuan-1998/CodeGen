import sys

def f(n, s, prefix_sum, memo):
    if n == 0:
        return 0
    if (n, s, prefix_sum) in memo:
        return memo[(n, s, prefix_sum)]
    if s > prefix_sum:
        return float('inf')
    
    a_i = prefix_sum // n
    x_i = min(a_i - s, 0)
    y_i = max(0, a_i - s)
    f1 = x_i * (a_i + 1) + y_i * (2*s - a_i - 1)
    f2 = x_i * (a_i - s) + y_i * ((prefix_sum + a_i) - 2*s - a_i - 1)
    
    return min(f(n-1, s, prefix_sum + a_i, memo), f(n-1, s, prefix_sum + a_i - 2*s, memo)) + f1

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(f(n, s, 0, {}))
