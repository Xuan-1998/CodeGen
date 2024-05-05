import sys

def f(n, memo):
    if n <= 2:
        return n
    if (n, 0) not in memo:
        memo[(n, 0)] = n * min(f(n-1, memo), f(n-3, memo))
    if (n, 1) not in memo:
        memo[(n, 1)] = min((f(n-1, memo), f(n-2, memo)))
    return memo[(n, 0)]

def solve(t, l, r):
    memo = {}
    res = 0
    for i in range(r-l+1):
        res += t * (f(l+i, memo) - l)
    return pow(10, 9)+7 - res

t, l, r = map(int, input().split())
print(solve(t, l, r))
