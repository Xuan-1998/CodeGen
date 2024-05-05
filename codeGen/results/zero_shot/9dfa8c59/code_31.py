code_block_start
import itertools

def generate_prime_permutations(n):
    # Generate all permutations of digits for number n
    perms = list(itertools.permutations(str(n)))
    
    # Filter out non-prime permutations
    prime_perms = [int(''.join(map(str, perm))) for perm in perms if is_prime(int(''.join(map(str, perm))))]
    
    return prime_perms

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max = int(input())  # Read n_max from stdin
k_perms = int(input())  # Read k_perms from stdin

prime_count = 0
smallest_prime = float('inf')
largest_prime = float('-inf')

for i in range(2, n_max):
    if is_prime(i):  # Check if number i is prime
        perms = generate_prime_permutations(i)
        if len(perms) == k_perms:  # Check if the number has exactly k_perms permutations
            prime_count += 1
            smallest_prime = min(smallest_prime, i)
            largest_prime = max(largest_prime, i)

print([prime_count, smallest_prime, largest_prime])  # Print the result to stdout

code_block_end
