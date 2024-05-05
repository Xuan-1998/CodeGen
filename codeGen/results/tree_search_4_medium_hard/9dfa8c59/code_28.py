===BEGIN SOLUTION===
import math
from collections import defaultdict

def count_prime_permutations(n_max, k_perms):
    # Create a set to store prime numbers below n_max
    prime_set = set()

    # Initialize the dictionary for permutation counts
    perm_counts = defaultdict(int)

    # Iterate over each number below n_max
    for num in range(2, n_max+1):
        # Check if the number is prime
        if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
            prime_set.add(num)

            # Calculate the number of permutations (factorial of digits)
            perm_count = math.factorial(len(str(num)))

            # Store the prime number and its permutation count
            perm_counts[num] = perm_count

    # Count prime numbers with exactly k_perms prime permutations
    count = 0
    smallest_prime = float('inf')
    largest_prime = 0

    for num, count in perm_counts.items():
        if count == k_perms:
            count += 1
            if num < smallest_prime:
                smallest_prime = num
            if num > largest_prime:
                largest_prime = num

    return [count, smallest_prime, largest_prime]

n_max, k_perms = map(int, input().split())
print(count_prime_permutations(n_max, k_perms))
===END SOLUTION===
