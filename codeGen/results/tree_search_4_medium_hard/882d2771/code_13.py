import sys

memo = {1: 0}
def f(n):
    if n in memo:
        return memo[n]
    min_comp = float('inf')
    for i in range(2, int(sys.getsizeof(1<<n)**.5) + 1):
        k = i * (1 << (n.bit_length() - 1))
        if k > n:
            break
        res = f(k)
        min_comp = min(min_comp, res + n - k)
    memo[n] = min_comp
    return min_comp

t, l, r = map(int, input().split())
ans = sum(t**i * f(l+i) for i in range(r-l+1)) % (10**9+7)
print(ans)
