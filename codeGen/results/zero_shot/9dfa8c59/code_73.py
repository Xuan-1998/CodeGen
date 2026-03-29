code
def is_prime(n):
    if n <= 1:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True

k_perms = int(input())
count = 0
smallest = largest = None
for prime in primes:
    perms = set()
    for i in range(len(str(prime))):
        for j in range(i + 1, len(str(prime)) + 1):
            perm = int("".join(sorted(str(prime)[i:j]))),)
            if is_prime(perm) and perm < n_max:
                perms.add(perm)
    if len(perms) == k_perms:
        count += 1
        smallest = min(smallest, prime) if smallest is None else smallest
        largest = max(largest, prime) if largest is None else largest

print([count, smallest, largest])
