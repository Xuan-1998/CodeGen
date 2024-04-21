def can_be_expressed(n):
    for x in range(n // 2020 + 1):
        if (n - 2020 * x) % 2021 == 0:
            return "YES"
    return "NO"

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(can_be_expressed(n))
