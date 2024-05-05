def apply_operations(n, m):
    count = 0
    while m > 0:
        if n < 10:
            count += 1
        elif n < 100:
            count += 2
        elif n < 1000:
            count += 3
        else:
            count += (n - 9) // 900 + 4
        m -= min(m, count)
        if n % 10 > 0:
            n //= 10
            count = 1
        else:
            n //= 10
    return (len(str(n)) + m - 1) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(apply_operations(n, m))
