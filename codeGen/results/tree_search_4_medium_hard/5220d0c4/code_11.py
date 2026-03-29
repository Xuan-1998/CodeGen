def beauty_of_array():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if all(x % p != 0 or p not in bad_primes for x in arr[:i]):
            dp[i] = min(dp[i-1], 1) + 1
        else:
            dp[i] = max(dp[i-1], 0)

    return dp[-1]

print(beauty_of_array())
