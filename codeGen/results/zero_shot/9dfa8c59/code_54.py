from collections import Counter

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max = int(input())
k_perms = int(input())

prime_numbers = [i for i in range(2, n_max) if is_prime(i)]

prime_permutations_count = Counter()

smallest_prime = float('inf')
largest_prime = -float('inf')

for prime in prime_numbers:
    perms = ''.join(sorted(str(prime)))  # Sort the digits
    perms_count = sum(is_prime(int(''.join(map(str, p)))) for p in permutations(perms))
    if perms_count == k_perms:
        smallest_prime = min(smallest_prime, int(''.join(map(str, prime))))
        largest_prime = max(largest_prime, int(''.join(map(str, prime))))

print([len(list(prime_permutations_count.elements())), smallest_prime, largest_prime])
