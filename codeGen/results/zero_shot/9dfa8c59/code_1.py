# Import necessary libraries
import sys
from sympy import isprime

def solve():
    # Read input from standard input
    n_max, k_perms = map(int, sys.stdin.readline().split())

    # Initialize count of prime numbers with k_perms prime permutations
    count = 0
    
    # Initialize smallest and largest prime numbers among them
    min_prime, max_prime = float('inf'), -1

    # Iterate over all numbers below n_max
    for num in range(2, n_max):
        # Check if the number is prime
        if isprime(num):
            # Convert the number to a string and sort its digits
            sorted_digits = "".join(sorted(str(num)))

            # Initialize count of prime permutations
            perms_count = 0

            # Generate all possible permutations of the digits
            for _ in range(len(set(sorted_digits))):
                permuted_num = int("".join(sorted_digits))
                
                # Check if the permutation is a prime number
                if isprime(permuted_num):
                    perms_count += 1
                
                # If we have found k_perms prime permutations, break
                if perms_count == k_perms:
                    break
            
            # Increment count of prime numbers with k_perms prime permutations
            if perms_count == k_perms:
                count += 1
                min_prime = min(min_prime, num)
                max_prime = max(max_prime, num)

    # Print the result to standard output
    print([count, min_prime, max_prime])

if __name__ == "__main__":
    solve()
