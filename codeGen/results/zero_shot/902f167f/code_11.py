n, m = map(int, input().split())
count = 0
while n > 0 and m > 0:
    if min(n, m) <= max(1, (n + m - 1) // 2):
        count += min(n, m)
        n -= min(n, m)
        m -= min(n, m)
    else:
        k = min(n, m)
        count += k
        n -= k
        m -= k
print(count)
