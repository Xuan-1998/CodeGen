import sys

def sieve_of_eratosthenes(n_max):
    # Create a boolean array, prime, of size n_max + 1
    prime = [True] * (n_max + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(n_max ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n_max + 1, p):
                prime[i] = False

    return [p for p in range(2, n_max + 1) if prime[p]]

def permutations(digits):
    # Base case: a single digit has only one permutation
    if len(digits) == 1:
        return [digits]

    result = []
    for i, digit in enumerate(digits):
        remaining_digits = digits[:i] + digits[i+1:]
        for perm in permutations(remaining_digits):
            result.append([digit] + perm)

    return result

def count_prime_permutations(n_max, k_perms):
    prime_numbers = sieve_of_eratosthenes(n_max)
    count = 0
    min_prime = max_prime = None

    for p in prime_numbers:
        perms = set(permutations(str(p)))
        if len(perms) == k_perms:
            count += 1
            if min_prime is None or p < min_prime:
                min_prime = p
            if max_prime is None or p > max_prime:
                max_prime = p

    return [count, min_prime, max_prime]

if __name__ == "__main__":
    n_max, k_perms = map(int, sys.stdin.readline().split())
    result = count_prime_permutations(n_max, k_perms)
    print(*result, sep=", ")
