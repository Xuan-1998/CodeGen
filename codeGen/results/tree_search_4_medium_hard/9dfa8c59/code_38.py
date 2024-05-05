from collections import Counter
import itertools

def solve():
    n_max, k_perms = map(int, input().split())
    
    # Base case: Return [0, 0, 0] when input number is less than or equal to 1
    if n_max <= 1:
        return [0, 0, 0]

    prime_numbers = set()
    for num in range(2, n_max):
        if all(num % i > 0 for i in range(2, int(num ** 0.5) + 1)):
            prime_numbers.add(num)

    count_of_primes = 0
    min_prime = float('inf')
    max_prime = 0

    for num in prime_numbers:
        digits = [int(digit) for digit in str(num)]
        perms = list(itertools.permutations(digits))
        perm_counts = Counter(tuple(perm) for perm in perms)
        
        if perm_counts.get(tuple(sorted(digits)), 0) == k_perms and len(perm_counts) == k_perms + 1:
            count_of_primes += 1
            min_prime = min(min_prime, num)
            max_prime = max(max_prime, num)

    return [count_of_primes, min_prime, max_prime]

print(solve())
