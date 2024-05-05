# Read input
n_max, k_perms = map(int, input().split())

# Initialize count of prime numbers with k_perms permutations
count = 0

# Initialize smallest and largest prime numbers found
smallest_prime = float('inf')
largest_prime = 0

for i in range(2, n_max):
    # Check if i is a prime number
    if is_prime(i):
        # Generate permutations of i
        perms = generate_permutations(str(i))
        
        # Count the number of permutations that are also prime numbers
        perm_count = sum(is_prime(int(p)) for p in perms)
        
        # If the count of prime permutations matches k_perms, increment the count and update smallest and largest prime numbers if necessary
        if perm_count == k_perms:
            count += 1
            smallest_prime = min(smallest_prime, i)
            largest_prime = max(largest_prime, i)

# Print the result
print([count, smallest_prime, largest_prime])
