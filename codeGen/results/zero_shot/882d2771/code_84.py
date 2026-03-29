def f(n):
    if n <= 2:
        return n - 1
    return (f((n + 1) // 2) + f(n // 2)) % (10**9 + 7)

t, l, r = map(int, input().split())
print(t * f(l) + sum([t * f(i) for i in range(l+1, r+1)]) - l * f(r))
