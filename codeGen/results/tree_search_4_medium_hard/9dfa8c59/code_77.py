def generate_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    return [p for p in range(2, n+1) if sieve[p]]

def count_prime_permutations(primes, k_perms, n_max):
    prime_perm_counts = {}

    for prime in primes:
        permutations = set()
        for digit in str(prime):
            for permutation in itertools.permutations(digit):
                permutation_str = ''.join(permutation)
                if int(permutation_str) < n_max and permutation_str in prime_perm_counts:
                    if prime_perm_counts[permutation_str] == k_perms:
                        prime_perm_counts[prime] = True
                        break
                elif int(permutation_str) < n_max and not prime_perm_counts.get(permutation_str, False):
                    permutations.add(permutation_str)

        for permutation in permutations:
            if permutation in prime_perm_counts:
                if prime_perm_counts[permutation] == k_perms:
                    prime_perm_counts[prime] = True
                    break

    count = sum(1 for prime in prime_perm_counts if prime_perm_counts[prime])
    smallest_prime = max((p for p in prime_perm_counts if prime_perm_counts[p]), default=0)
    largest_prime = min((p for p in prime_perm_counts if prime_perm_counts[p]), default=n_max)

    return [count, smallest_prime, largest_prime]

n_max, k_perms = map(int, input().split())
primes = generate_primes(n_max)
result = count_prime_permutations(primes, k_perms, n_max)
print(*result)
