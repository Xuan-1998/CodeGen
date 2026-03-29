import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    str_n = str(n)
    perms = set()
    for p in itertools.permutations(str_n):
        perms.add(''.join(p))
    return perms

def find_primes(n_max, k_perms):
    count = 0
    smallest = float('inf')
    largest = float('-inf')
    for p in range(2, n_max + 1):
        if is_prime(p):
            perms = permute_digits(p)
            if len(perms) == k_perms:
                count += 1
                smallest = min(smallest, p)
                largest = max(largest, p)
    return [count, smallest, largest]

n_max = int(input())
k_perms = int(input())
result = find_primes(n_max, k_perms)
print(*result)
