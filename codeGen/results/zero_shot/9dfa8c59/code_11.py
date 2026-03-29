# Read input
n_max, k_perms = map(int, input().split())

# Initialize count, smallest_prime, largest_prime
count = 0
smallest_prime = float('inf')
largest_prime = -1

# Iterate over all numbers less than n_max
for num in range(2, n_max):
    # Check if the number is prime
    if is_prime(num):
        # Find the permutations of the digits
        perms = get_permutations(str(num))
        
        # Check if the number has k_perms prime permutations
        if len([p for p in perms if is_prime(int(p))]) == k_perms:
            # Increment count, update smallest_prime and largest_prime
            count += 1
            smallest_prime = min(smallest_prime, num)
            largest_prime = max(largest_prime, num)

# Print the result
print([count, smallest_prime, largest_prime])
