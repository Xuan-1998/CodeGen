def max_beauty(n, m, arr, bad_primes):
    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        min_prime_divisor = next((p for p in range(2, int(arr[i] ** 0.5) + 1) if arr[i] % p == 0), None)
        if min_prime_divisor is not None:
            good_beauty = dp[i - 1][1] + (min_prime_divisor > 1 and 1 or 0)
            bad_beauty = dp[i - 1][0]
            if arr[i] in bad_primes:
                dp[i][1] = max(dp[i - 1][1], good_beauty)
                dp[i][0] = min(dp[i - 1][0], bad_beauty)
            else:
                dp[i][1] = max(dp[i - 1][1], good_beauty, bad_beauty + (min_prime_divisor > 1 and 1 or 0))
                dp[i][0] = min(dp[i - 1][0], bad_beauty)
    return max(dp[n][0], dp[n][1])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
