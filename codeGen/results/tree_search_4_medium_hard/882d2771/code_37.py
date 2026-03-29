code
t, l, r = map(int, input().split())
MOD = 10**9 + 7

def solve():
    memo = {1: 0}
    def f(n):
        if n not in memo:
            memo[n] = min(f(m) + f(n - m) for m in range(1, n))
        return memo[n]

    ans = sum(t * (f(i) - i) for i in range(l, r + 1)) % MOD
    print(ans)

solve()
