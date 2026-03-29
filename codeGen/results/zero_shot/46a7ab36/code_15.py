tot = 0

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    ps = [1] * ((n + 1) // 2)
    for i in range(1, (n + 1) // 2):
        ps[i] = (ps[i - 1] * (2 * i)) % (10**8 + 7)

    if n % 2 != 0:
        ps[-1] = ((n // 2) + 1) * (10**5)

    psm = [1] * (m + 1)
    for i in range(1, m + 1):
        psm[i] = (psm[i - 1] * (i)) % (10**8 + 7)

    if m % 2 != 0:
        psm[-1] = ((m // 2) + 1)

    for i in range(1, min(m + 1, n // 2) + 1):
        tot = (tot * psm[i]) % (10**8 + 7)
        if 2 * i > n:
            tot = (tot * ps[(n - 1) // 2]) % (10**8 + 7)

    if m >= n // 2:
        tot = (tot * ((m - n // 2) + 1)) % (10**8 + 7)

    print(tot)
