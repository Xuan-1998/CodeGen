from collections import defaultdict

def solve():
    n_max, k_perms = map(int, input().split())
    primes = sieve(n_max)
    
    count = 0
    smallest_prime = largest_prime = None
    
    for prime in primes:
        digit_counts = get_digit_counts(prime)
        perms = get_permutations(digit_counts)
        
        if len(perms) == k_perms:
            count += 1
            if smallest_prime is None or prime < smallest_prime:
                smallest_prime = prime
            if largest_prime is None or prime > largest_prime:
                largest_prime = prime
                
    print(count, smallest_prime, largest_prime)

def sieve(n_max):
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n_max + 1, i):
                sieve[j] = False
                
    return [i for i in range(2, n_max + 1) if sieve[i]]

def get_digit_counts(n):
    digit_counts = defaultdict(int)
    
    while n:
        digit = n % 10
        digit_counts[digit] += 1
        n //= 10
        
    return dict(digit_counts)

def get_permutations(digit_counts):
    perms = set()
    
    def generate_perms(digits, current_perm):
        if len(digits) == 0:
            perms.add(tuple(sorted(current_perm)))
        else:
            for digit in digits:
                new_digits = digits.copy()
                new_digits.remove(digit)
                generate_perms(new_digits, current_perm + [digit])
                
    generate_perms(digit_counts.keys(), [])
    
    return list(perms)

if __name__ == "__main__":
    solve()
