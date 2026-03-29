import itertools

def get_prime_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    for p in itertools.permutations(digits):
        num = int(''.join(map(str, p)))
        if is_prime(num):
            permutations.add(num)
    return len(permutations)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
smallest = float('inf')
largest = float('-inf')

for p in sieve_of_eratosthenes(n_max):
    if get_prime_permutations(p) == k_perms:
        count += 1
        smallest = min(smallest, p)
        largest = max(largest, p)

print([count, smallest, largest])
