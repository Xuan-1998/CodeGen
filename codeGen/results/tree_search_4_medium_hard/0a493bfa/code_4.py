from collections import defaultdict

def prime_divisors(n):
    i = 2
    divs = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            divs.add(i)
    if n > 1:
        divs.add(n)
    return divs

def max_beauty(a, b):
    memo = defaultdict(int)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return 0
        if j == 0:
            return sum(a[:i])
        p = min(a[i - 1], *b[:j])
        while p and p not in b[:j]:
            p = prime_divisors(p)
            p -= set(b[:j])
            p = max(p)
        return dp(i - 1, j) + (a[i - 1] if p else 0)

    return dp(len(a), len(b))

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_beauty(a, b))
