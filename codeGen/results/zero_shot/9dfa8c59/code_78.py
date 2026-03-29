def sieve_of_eratosthenes(n_max):
    # Initialize a boolean array, prime, of size n_max + 1
    prime = [True] * (n_max + 1)
    
    # 0 and 1 are not prime numbers
    prime[0] = prime[1] = False
    
    # Iterate from 2 to sqrt(n_max)
    for p in range(2, int(n_max ** 0.5) + 1):
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n_max + 1, p):
                prime[i] = False
    
    return [p for p in range(2, n_max + 1) if prime[p]]

def count_prime_permutations(n):
    prime_perms = set()
    for p in str(n):
        prime_perms.add(int(''.join(sorted(p))))
    
    return len([p for p in prime_perms if is_prime(p)])

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max, k_perms = map(int, input().split())
prime_numbers = sieve_of_eratosthenes(n_max)

count = 0
smallest = largest = None

for p in prime_numbers:
    perms_count = count_prime_permutations(p)
    if perms_count == k_perms:
        count += 1
        if smallest is None or p < smallest:
            smallest = p
        if largest is None or p > largest:

print([count, smallest, largest])
