def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n):
    perms = set()
    def permute(s):
        if len(s) == 1:
            perms.add(int(s))
            return
        for i in range(len(s)):
            c = s[i]
            remain = s[:i] + s[i+1:]
            permute(remain + c)
    permute(str(n))
    return [p for p in perms if is_prime(p)]

def find_primes(n_max, k_perms):
    primes_with_k_perms = []
    for i in range(2, n_max):
        if is_prime(i):
            perms = prime_permutations(i)
            if len(perms) == k_perms:
                primes_with_k_perms.append(i)
    return [len(primes_with_k_perms), min(primes_with_k_perms) if primes_with_k_perms else 0, max(primes_with_k_perms) if primes_with_k_perms else 0]

n_max = int(input())
k_perms = int(input())

result = find_primes(n_max, k_perms)
print(*result, sep='\n')
