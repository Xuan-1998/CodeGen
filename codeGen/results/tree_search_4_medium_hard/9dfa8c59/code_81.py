from collections import defaultdict
from itertools import permutations

def solve():
    n_max, k_perms = map(int, input().split())
    
    # Handle edge cases
    if n_max < 2 or k_perms > 3:
        return [0, 0, 0]
    
    count = 0
    smallest_prime = float('inf')
    largest_prime = 0
    
    memo = defaultdict(dict)
    
    def is_prime(n):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result = False
                memo[n] = result
                return result
        
        result = True
        memo[n] = result
        return result
    
    def count_permutations(n):
        digits = [int(digit) for digit in str(n)]
        perms = set(permutations(digits))
        
        if len(perms) == k_perms:
            return 1
        else:
            return 0
    
    for p in range(2, n_max + 1):
        if is_prime(p):
            if count_permutations(p) == 1:
                count += 1
                smallest_prime = min(smallest_prime, p)
                largest_prime = max(largest_prime, p)
    
    return [count, smallest_prime, largest_prime]

print(*solve(), sep='\n')
