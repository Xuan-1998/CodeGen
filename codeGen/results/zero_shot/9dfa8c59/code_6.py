import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max = int(input())
k_perms = int(input())

prime_numbers = [i for i in range(2, n_max + 1) if is_prime(i)]

prime_perms_counts = {}
for prime in prime_numbers:
    perms_count = generate_prime_permutations(prime)
    prime_perms_counts[prime] = perms_count

count = 0
smallest_prime = float('inf')
largest_prime = float('-inf')
for prime, perms_count in prime_perms_counts.items():
    if perms_count == k_perms:
        count += 1
        smallest_prime = min(smallest_prime, prime)
        largest_prime = max(largest_prime, prime)

result = [count, smallest_prime, largest_prime]
print(result)

def generate_prime_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    for p in itertools.permutations(digits):
        permutation = int(''.join(map(str, p)))
        if is_prime(permutation):
            permutations.add(permutation)
    return len(permutations)
