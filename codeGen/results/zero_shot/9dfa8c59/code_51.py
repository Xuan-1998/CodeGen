import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]"
    prime = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if prime[p]:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]

def prime_permutations(n):
    permutations = set()
    for digit in str(n):
        for permutation in itertools.permutations(str(n).replace(digit, '')):
            permutations.add(int(''.join(permutation) + digit))
    return list(set(filter(lambda x: x < n and is_prime(x), permutations)))

def count_prime_permutations(n_max, k_perms):
    prime_numbers = sieve_of_eratosthenes(n_max)
    count = 0
    min_prime = float('inf')
    max_prime = float('-inf')
    for p in prime_numbers:
        if len(prime_permutations(p)) == k_perms:
            count += 1
            if p < min_prime:
                min_prime = p
            if p > max_prime:
                max_prime = p
    return [count, min_prime, max_prime]

n_max, k_perms = map(int, sys.stdin.read().strip().split())
print(count_prime_permutations(n_max, k_perms))
