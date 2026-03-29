def f(n):
    return n * (n - 1) // 2 % (10**9 + 7)

t, l, r = map(int, input().split())
result = 0
for i in range(t):
    if i == 0:
        result += f(l) % (10**9 + 7)
    else:
        result += f(l + i) - f(l + i - 1)
result -= l * f(r) % (10**9 + 7)
print(result % (10**9 + 7))
