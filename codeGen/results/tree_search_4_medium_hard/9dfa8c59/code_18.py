from collections import defaultdict

def solve():
    n_max, k_perms = map(int, input().split())
    primes = set()
    perms = defaultdict(int)
    is_prime = [False] * (n_max + 1)

    def prime_permutations(n):
        digits = list(str(n))
        for p in range(len(digits)):
            for q in range(p + 1, len(digits)):
                perm = int(''.join(sorted(digits[:p] + digits[p:q] + digits[q:])))
                perms[perm] += 1
        return n

    def is_prime_num(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, n_max + 1):
        if is_prime_num(i):
            primes.add(i)
            prime_permutations(i)

    count = sum(1 for p in primes if perms[p] == k_perms and is_prime_num(p))
    min_prime = max_prime = float('inf')
    for p in primes:
        if perms[p] == k_perms and is_prime_num(p):
            min_prime = min(min_prime, p)
            max_prime = max(max_prime, p)

    print([count, min_prime, max_prime])

if __name__ == "__main__":
    solve()
