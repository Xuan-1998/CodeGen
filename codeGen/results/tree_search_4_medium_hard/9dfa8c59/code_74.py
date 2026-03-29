import math

def prime_permutations(n_max, k_perms):
    # Generate all prime numbers up to n_max
    primes = []
    for p in range(2, n_max + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(p)) + 1):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)

    # Check the number of permutations for each prime number
    perms_count = {}
    for prime in primes:
        digits = [int(x) for x in str(prime)]
        unique_digits = set(digits)
        perms = math.factorial(len(unique_digits))
        if len(unique_digits) == k_perms:
            perms_count[prime] = perms

    # Count the total number of prime numbers that meet the condition
    count = sum(1 for prime, _ in perms_count.items())

    # Find the smallest and largest prime numbers among those that meet the condition
    smallest_prime = min(perms_count.keys())
    largest_prime = max(perms_count.keys())

    return [count, smallest_prime, largest_prime]

# Example usage:
n_max = int(input())
k_perms = int(input())
result = prime_permutations(n_max, k_perms)
print(*result, sep='\n')
