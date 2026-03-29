def solve():
    n_max, k_perms = map(int, input().split())

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_permutations(n):
        digits = [int(d) for d in str(n)]
        permutations = set()
        for p in itertools.permutations(digits):
            permutation = int(''.join(map(str, p)))
            permutations.add(permutation)
        return len(permutations)

    primes = []
    for n in range(n_max, 1, -1):
        if is_prime(n) and count_permutations(n) == k_perms:
            primes.append(n)

    print([len(primes), min(primes), max(primes)]) if primes else print(0, 0, 0)
