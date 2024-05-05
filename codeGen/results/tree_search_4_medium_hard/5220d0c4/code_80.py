def max_beauty(n, primes, bad_primes):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    good_primes = [p for p in primes if p not in bad_primes]
    
    # Initialize the base case: beauty value of an empty subarray is 0
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            last_elem = primes[j - 1]
            if last_elem in good_primes:
                # If the last element is a good prime, consider its minimum prime divisor
                dp[i][j] = max(dp[i - 1][j - 1] + (1 if min_prime_divisor(last_elem) in good_primes else -1), dp[i - 1][j])
            else:
                # If the last element is not a good prime, consider only its minimum prime divisor
                dp[i][j] = max(dp[i - 1][j - 1] + (1 if min_prime_divisor(last_elem) in good_primes else -1), dp[i - 1][j])
    
    return max(max(row) for row in dp)

def min_prime_divisor(n):
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return p
    return n

if __name__ == "__main__":
    n, m = map(int, input().split())
    primes = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(max_beauty(n, primes, bad_primes))
