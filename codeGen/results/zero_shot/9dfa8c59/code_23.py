import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]"
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    return [p for p in range(2, n) if prime[p]]

def count_prime_permutations(primes, k_perms):
    count = 0
    smallest = float('inf')
    largest = float('-inf')
    
    for prime in primes:
        perm_count = len([str(p) for p in range(2, prime) if str(p) == ''.join(sorted(str(p))) and p < n_max])
        
        if perm_count == k_perms:
            count += 1
            smallest = min(smallest, prime)
            largest = max(largest, prime)
    
    return [count, smallest, largest]

n_max = int(sys.stdin.readline().strip())
k_perms = int(sys.stdin.readline().strip())

primes = sieve_of_eratosthenes(n_max)

result = count_prime_permutations(primes, k_perms)

print(*result, sep='\n')
