from collections import defaultdict

def prime_permutations(n_max, k_perms):
    # Initialize the hash set for prime numbers and the dictionary for permutation counts
    primes = set()
    perms_counts = defaultdict(int)

    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Iterate over each number below n_max to count its permutations
    for num in range(2, n_max):
        if is_prime(num):
            primes.add(num)

    for prime in primes:
        # Count the number of prime permutations for each prime number
        for perm in set(int(''.join(sorted(str(prime))))) - {prime}:
            if is_prime(perm) and len(set(int(digit) for digit in str(perm))) == len(str(perm)):
                perms_counts[prime] += 1

    # Find the smallest and largest prime numbers among those with k_perms prime permutations below n_max
    count = sum(1 for count in perms_counts.values() if count == k_perms)
    min_prime, max_prime = min(prime for prime, count in perms_counts.items() if count == k_perms), \
                            max(prime for prime, count in perms_counts.items() if count == k_perms)

    # Return the count, smallest, and largest as the final output
    return [count, min_prime, max_prime]

# Read input from standard input
n_max, k_perms = map(int, input().split())

# Print the output to standard output
print(prime_permutations(n_max, k_perms))
