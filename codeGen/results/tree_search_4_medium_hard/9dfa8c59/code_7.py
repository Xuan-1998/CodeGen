import sys

def count_prime_permutations(n_max, k_perms):
    # Initialize the set of primes and the dictionary for memoization
    primes = set()
    memo = {}

    def is_prime(num):
        if num in memo:
            return memo[num]
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                memo[num] = False
                return True
        memo[num] = True
        return True

    # Generate all prime numbers below n_max
    for num in range(2, n_max):
        if is_prime(num):
            primes.add(num)

    # Initialize the count and smallest/largest prime numbers with k_perms permutations
    count = 0
    smallest_prime = float('inf')
    largest_prime = -float('inf')

    # Iterate over all prime numbers below n_max and check for k_perms permutations
    for num in sorted(primes):
        if is_prime(num):
            perms = set()
            def get_permutations(n, used=None):
                nonlocal perms
                if used is None:
                    used = set()
                if len(used) == 0:
                    return [str(n)]
                result = []
                for i in range(len(str(n))):
                    if str(n)[i] not in used:
                        new_used = used.copy()
                        new_used.add(str(n)[i])
                        for perm in get_permutations(int(''.join(sorted(str(n)[i+1:]+new_used))), new_used):
                            result.append(str(n) + perm)
                return result
            for perm in get_permutations(num):
                if is_prime(int(perm)):
                    perms.add(perm)

            # Check if the number has k_perms permutations and update the count, smallest/largest prime numbers
            if len(perms) == k_perms:
                count += 1
                smallest_prime = min(smallest_prime, num)
                largest_prime = max(largest_prime, num)

    return [count, smallest_prime, largest_prime]

# Receive inputs from stdin and print the answer to stdout
n_max, k_perms = map(int, input().split())
print(*count_prime_permutations(n_max, k_perms), sep='\n')
