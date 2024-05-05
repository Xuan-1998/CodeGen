import sys

def calculate_f(n):
    f = [0] * (n + 1)
    for i in range(2, n + 1):
        f[i] = min(f[i-1], f[i-2] + 2)
    return f[n]

t, l, r = map(int, input().split())
print(sum(t[i] * calculate_f(l+i) - (l+i)*calculate_f(l+i) for i in range(r-l+1)) % (10**9 + 7))
