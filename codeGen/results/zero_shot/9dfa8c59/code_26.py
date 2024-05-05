import sys

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def is_prime_permutation(num, k_perms):
    perms = set()
    while num:
        perm = int("".join(sorted(map(str, list(num)))))
        if is_prime[perm]:
            perms.add(perm)
        num //= 10
    return len(perms) == k_perms

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

is_prime = sieve_of_eratosthenes(n_max)
count = smallest = largest = 0
for i in range(2, n_max):
    if is_prime[i] and is_prime_permutation(i, k_perms):
        count += 1
        if not smallest:
            smallest = i
        largest = i

print([count, smallest, largest])
