def has_prime_permutations(n_max, k_perms):
    primes = set()
    for i in range(2, n_max + 1):
        if all(i % j > 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.add(i)

    dp = {i: 0 for i in primes}
    for prime in primes:
        count = 1
        if len(str(prime)) > 1:
            for digit in str(prime):
                count *= len(set(int(digit) * 10 + int(x) for x in range(10)))
        dp[prime] = count

    k_count = sum(1 for count in dp.values() if count == k_perms)
    smallest_prime = min((prime for prime, count in dp.items() if count == k_perms), default=None)
    largest_prime = max((prime for prime, count in dp.items() if count == k_perms), default=None)

    return [k_count, smallest_prime, largest_prime]
