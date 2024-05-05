import itertools
from collections import defaultdict

def count_prime_permutations(n_max, k_perms):
    # Initialize dp array with zeros
    dp = [0] * (n_max + 1)
    
    for p in range(2, n_max + 1):
        if is_prime(p):
            str_p = str(p)
            perms = list(itertools.permutations(str_p))
            count = len(set(''.join(map(str, perm)) for perm in perms))
            
            if count == k_perms:
                dp[p] += 1
    
    # Find the smallest and largest prime numbers with exactly k_perms permutations
    first_non_zero_index = next((i for i, x in enumerate(dp) if x), None)
    
    if first_non_zero_index is None:
        return [0, 0, 0]
    
    smallest_prime = next(i for i, x in enumerate(range(2, n_max + 1)) if is_prime(i) and dp[i] == k_perms)
    largest_prime = max(i for i in range(first_non_zero_index, n_max + 1) if is_prime(i) and dp[i] == k_perms)
    
    return [dp[n_max], smallest_prime, largest_prime]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n_max, k_perms = map(int, input().split())
    print(count_prime_permutations(n_max, k_perms))
