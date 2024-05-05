def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]

def get_prime_permutations(prime):
    perms = set()
    for p in str(prime):
        for perm in itertools.permutations(p):
            perms.add(''.join(map(str, perm)))
    return len(perms)

def count_prime_numbers(n_max, k_perms):
    primes = sieve_of_eratosthenes(n_max)
    count = 0
    min_prime = float('inf')
    max_prime = 0

    for p in primes:
        perms = get_prime_permutations(p)
        if perms == k_perms:
            count += 1
            min_prime = min(min_prime, p)
            max_prime = max(max_prime, p)

    return [count, min_prime, max_prime]

if __name__ == "__main__":
    n_max = int(input())
    k_perms = int(input())
    result = count_prime_numbers(n_max, k_perms)
    print(*result)
