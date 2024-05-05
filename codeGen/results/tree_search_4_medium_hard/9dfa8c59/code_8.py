import sys

def read_input():
    n_max, k_perms = map(int, input().split())
    return n_max, k_perms

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int((n**0.5)) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [p for p in range(n + 1) if sieve[p]]

def permutations(num):
    digits = list(map(int, str(num)))
    perms = set()
    def permute(digits):
        if len(digits) == 1:
            perms.add(int(''.join(map(str, digits))))
        else:
            for i, d in enumerate(digits):
                remaining_digits = digits[:i] + digits[i+1:]
                for p in permute(remaining_digits):
                    yield [d] + p
    for p in permute(digits):
        perms.add(int(''.join(map(str, p))))
    return perms

def solve(n_max, k_perms):
    primes = set(sieve_of_eratosthenes(n_max))
    prime_counts = {}
    for num in primes:
        perms = permutations(num)
        count = 0
        for perm in perms:
            if perm in primes:
                count += 1
        if count == k_perms:
            prime_counts[num] = count

    if not prime_counts:
        return [0, 0, 0]
    min_prime = max_prime = count = prime_counts.popitem()[0]

    for num in sorted(prime_counts):
        if prime_counts[num] > count or (prime_counts[num] == count and num < min_prime):
            min_prime = num
        if prime_counts[num] > count:
            max_prime = num
            break

    return [len(prime_counts), min_prime, max_prime]

if __name__ == "__main__":
    n_max, k_perms = read_input()
    print(*solve(n_max, k_perms), sep='\n')
