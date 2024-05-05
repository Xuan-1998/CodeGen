def beauty_fair(r):
    MOD = 10**9 + 7

    @lru_cache(None)
    def f(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return min(f(x-1) + 1, f(x-2) + 2)

    ans = (f(r) - l * f(r)) % MOD
    return ans

# Read input from standard input
t, l, r = map(int, input().split())

print(beauty_fair(r))
