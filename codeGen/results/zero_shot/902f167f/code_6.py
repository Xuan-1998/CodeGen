n, m = map(int, input().split())
res = 0
for i in range(1, min(n, m) + 1):
    a = n // i
    b = m // i
    if i * a == n and i * b == m:
        res = max(a, b)
        break
print(res)
