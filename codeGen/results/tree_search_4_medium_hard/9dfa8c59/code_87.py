import itertools

def solve(n_max, k_perms):
    primes = [i for i in range(2, n_max+1) if all(i % j > 0 for j in range(2, int(i**0.5)+1))]
    
    count = 0
    smallest_prime = float('inf')
    largest_prime = 0
    
    for prime in primes:
        perms = set(int(''.join(map(str, p))) for p in itertools.permutations(str(prime)))
        
        if len([p for p in perms if p <= n_max and is_prime(p)]) == k_perms:
            count += 1
            smallest_prime = min(smallest_prime, prime)
            largest_prime = max(largest_prime, prime)
    
    return [count, smallest_prime, largest_prime]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Example usage:
n_max = int(input())
k_perms = int(input())
result = solve(n_max, k_perms)
print(*result)
