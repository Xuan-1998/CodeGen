import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    digits = [int(d) for d in str(n)]
    permutations = set()
    for p in itertools.permutations(digits):
        permutation = int(''.join(map(str, p)))
        permutations.add(permutation)
    return len(permutations)

n_max, k_perms = map(int, input().split())
prime_numbers = []
for i in range(2, n_max + 1):
    if is_prime(i) and permute_digits(i) == k_perms:
        prime_numbers.append(i)

count = len(prime_numbers)
smallest = min(prime_numbers) if count > 0 else 0
largest = max(prime_numbers) if count > 0 else 0

print([count, smallest, largest])
