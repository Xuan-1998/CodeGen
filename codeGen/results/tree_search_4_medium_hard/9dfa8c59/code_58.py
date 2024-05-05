import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
                
    return [p for p in range(2, n + 1) if prime[p]]

def get_permutations_count(num):
    # Calculate the number of permutations for a given num
    digits = str(num)
    unique_digits = set(digits)
    permutations_count = 1
    
    for digit in unique_digits:
        permutations_count *= len(str(digit))
        
    return permutations_count

def main():
    n_max, k_perms = map(int, input().split())
    
    # Generate prime numbers up to n_max
    primes = sieve_of_eratosthenes(n_max)
    
    count = 0
    min_prime = max_prime = 0
    
    for p in primes:
        if get_permutations_count(p) == k_perms:
            count += 1
            min_prime = min(min_prime, p)
            max_prime = max(max_prime, p)
            
    print([count, min_prime, max_prime])

if __name__ == "__main__":
    main()
