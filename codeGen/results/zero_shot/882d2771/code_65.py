def f(n):
    return n & -n

t, l, r = map(int, input().split())
result = sum(t[i] * f(l + i) for i in range(r - l + 1)) - l * f(r)
print(result % (10**9 + 7))
