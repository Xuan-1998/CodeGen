from functools import lru_cache

def prime_permutations(n, k):
    @lru_cache(None)
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    count = 0
    min_prime = float('inf')
    max_prime = 0
    for i in range(2, n+1):
        if is_prime(i):
            perms = set()
            num = str(i)
            for p in prime_permutations(num):
                perms.add(p)
            if len(perms) == k:
                count += 1
                min_prime = min(min_prime, int(p))
                max_prime = max(max_prime, int(p))

    return [count, min_prime, max_prime]

n_max, k_perms = map(int, input().split())
print(prime_permutations(n_max, k_perms))
