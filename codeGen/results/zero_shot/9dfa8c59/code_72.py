def find_primes(n_max, k_perms):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_counts = {}
    prime_permutations = {}

    for num in range(2, n_max):
        if is_prime(num):
            digits = [int(digit) for digit in str(num)]
            perms = set(permutations(digits))
            if len(perms) == k_perms:
                prime_counts[num] = 1
                prime_permutations[num] = perms

    count = len(prime_counts)
    min_prime = min(prime_counts.keys())
    max_prime = max(prime_counts.keys())

    return [count, min_prime, max_prime]
