import sys
from collections import defaultdict

def solve():
    n_max, k_perms = map(int, input().split())
    
    if n_max <= 1 or k_perms > 3:
        return [0, 0, 0]

    primes = set()
    for num in range(2, int(n_max**0.5) + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(num)
    
    count = 0
    min_prime = max_prime = None
    for prime in primes:
        perms_count = defaultdict(int)
        for p in str(prime):
            p = int(p)
            perms_count[p] += 1
        
        has_k_perms = any(count == k_perms for count in perms_count.values())
        
        if has_k_perms:
            count += 1
            min_prime = min(min_prime, prime) if min_prime is None else min_prime
            max_prime = max(max_prime, prime)
    
    return [count, min_prime, max_prime]

print(*solve(), sep=' ')
