def max_beauty(n, bad_primes, arr):
    memo = {}

    # Initialize the table with base case (empty subarray)
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        min_divisor = None
        is_bad_prime = False

        # Compute the minimum prime divisor of the current element
        for p in bad_primes:
            if arr[i - 1] % p == 0:
                min_divisor = p
                is_bad_prime = True
                break

        # If the current element is not a bad prime, use the previous state
        if not is_bad_prime:
            dp[i][is_bad_prime] = max(dp[i - 1][is_bad_prime], dp[i - 1][0])
        else:
            # Compute the beauty value for this subarray and store it in memo
            state = (min_divisor, is_bad_prime)
            if state not in memo:
                memo[state] = 0
                for j in range(i):
                    if arr[j] % min_divisor == 0:
                        memo[state] += 1

            dp[i][is_bad_prime] = max(dp[i - 1][is_bad_prime], memo[state])

    return dp[n][1]

n, m = map(int, input().split())
bad_primes = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(max_beauty(n, bad_primes, arr))
