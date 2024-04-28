n, m = map(int, input().split())
res = 0
while n > 1 or m > 1:
    if n >= m:
        n -= m
    else:
        m -= n
    res += 1
print(res)
