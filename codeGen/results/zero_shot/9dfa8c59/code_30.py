from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_permutations(n_max, k_perms):
    prime_numbers = [i for i in range(2, n_max+1) if is_prime(i)]
    
    count = 0
    smallest = float('inf')
    largest = 0
    
    for prime in prime_numbers:
        digits = [int(x) for x in str(prime)] 
        perms = set(int(''.join(map(str, p))) for p in permutations(digits))
        
        if len([p for p in perms if is_prime(p)]) == k_perms:
            count += 1
            smallest = min(smallest, prime)
            largest = max(largest, prime)
    
    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(find_prime_permutations(n_max, k_perms))
