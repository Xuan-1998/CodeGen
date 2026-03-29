# Your code

dp = {}

def f(i):
    if i in dp:
        return dp[i]
    beauty = 0
    for j in range(i, n+1):
        p = min(gcd(j, k) for k in range(2, j))
        if p not in bad_primes:
            beauty = max(beauty, f(j // p) + j)
        else:
            beauty = max(beauty, f(j // p) - j)
    dp[i] = beauty
    return beauty

n, m = map(int, input().split())
bad_primes = set(map(int, input().split()))
a = list(map(int, input().split()))

print(f(1))
