import sys

def get_prime_permutations(n_max):
    # Create a set of prime numbers below n_max
    primes = set()
    for i in range(2, int(n_max ** 0.5) + 1):
        if all(i % j > 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.add(i)
    
    # Create a dictionary storing permutation counts
    perms = {}
    for prime in primes:
        perm_count = calculate_permutations(prime)
        perms[prime] = perm_count
    
    # Initialize counters for total count and smallest/largest prime numbers
    total_count = 0
    min_prime = max_prime = 0
    
    # Iterate over the dictionary to find prime numbers with k_perms permutations
    for prime, perm_count in perms.items():
        if perm_count == k_perms:
            total_count += 1
            min_prime = min(min_prime, prime)
            max_prime = max(max_prime, prime)
    
    return [total_count, min_prime, max_prime]

def calculate_permutations(n):
    # TO DO: Implement a recursive function to calculate permutation counts
    pass

# Read input from stdin
n_max, k_perms = map(int, sys.stdin.readline().split())

# Call the get_prime_permutations function and print the result
result = get_prime_permutations(n_max)
print(*result, sep=' ')
