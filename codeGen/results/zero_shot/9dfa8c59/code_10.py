import sys

def sieve_of_eratosthenes(n_max):
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int((n_max ** 0.5)) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False
    return [p for p in range(2, n_max + 1) if sieve[p]]

def count_prime_permutations(prime_numbers, k_perms):
    prime_perm_counts = {}
    for prime in prime_numbers:
        perm_count = 0
        prime_digits = str(prime)
        for _ in range(len(prime_digits)):
            permutations = [int(''.join(sorted(permutation))) for permutation in itertools.permutations(prime_digits)]
            perm_count += sum(1 for p in permutations if is_prime(p))
        if perm_count == k_perms:
            print(f"Count: {prime_perm_counts.get(prime, 0) + 1}")
            prime_perm_counts[prime] = prime_perm_counts.get(prime, 0) + 1
    return list(prime_perm_counts.keys())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n_max = int(sys.stdin.readline())
    k_perms = int(sys.stdin.readline())
    prime_numbers = sieve_of_eratosthenes(n_max)
    smallest_prime, largest_prime = None, None
    count = 0
    for prime in prime_numbers:
        perm_count = 0
        prime_digits = str(prime)
        for _ in range(len(prime_digits)):
            permutations = [int(''.join(sorted(permutation))) for permutation in itertools.permutations(prime_digits)]
            perm_count += sum(1 for p in permutations if is_prime(p))
        if perm_count == k_perms:
            count += 1
            smallest_prime, largest_prime = min((smallest_prime, prime)), max((largest_prime, prime))
    print([count, smallest_prime, largest_prime])
