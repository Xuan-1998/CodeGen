def dp(n, k, memo):
    if n == 2:
        return 0
    if (n, k) in memo:
        return memo[(n, k)]
    res = float('inf')
    for p in prime_factors(k):
        for u in range(1, n):
            for v in range(u+1, n):
                res = min(res, dp(min(v, n-1), k//p) + dp(max(v, 0), k//p) + (u != 0 and (v - u)))
    memo[(n, k)] = res
    return res

def prime_factors(k):
    factors = []
    i = 2
    while i * i <= k:
        if k % i:
            i += 1
        else:
            k //= i
            factors.append(i)
    if k > 1:
        factors.append(k)
    return factors

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    memo = {}
    print((dp(n, k, memo) + n - 2) % (10**9 + 7))
