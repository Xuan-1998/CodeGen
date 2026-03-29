import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_permutations(p):
    perm_count = 0
    for perm in itertools.permutations(str(p)):
        p_perm = int("".join(perm))
        if is_prime(p_perm):
            perm_count += 1
    return perm_count

def find_k_perms_primes(n_max, k_perms):
    count = 0
    min_p = float('inf')
    max_p = float('-inf')
    for p in range(2, n_max + 1):
        if is_prime(p):
            perm_count = count_prime_permutations(p)
            if perm_count == k_perms:
                count += 1
                min_p = min(min_p, p)
                max_p = max(max_p, p)
    return [count, min_p, max_p]

n_max, k_perms = map(int, input().split())
print(find_k_perms_primes(n_max, k_perms))
