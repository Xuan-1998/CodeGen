def f(n):
    # Implement the logic for f(n) here
    pass

t, l, r = map(int, input().split())
result = 0
for i in range(t):
    if l <= i <= r:
        result += (i - l + 1) * f(i)
    else:
        result += t0 * f(l)

print(result % (10**9 + 7))
