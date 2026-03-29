def f(n):
    return n - 1

t, l, r = map(int, input().split())

print((t * sum(f(i) for i in range(l, r+1)) - l * f(r)) % (10**9 + 7))
