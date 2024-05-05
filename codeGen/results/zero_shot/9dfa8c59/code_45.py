import sys
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_permutations(n):
    digits = [int(d) for d in str(n)]
    perms = set()
    for p in permutations(digits):
        perms.add(int(''.join(map(str, p))))
    return perms

def main():
    n_max, k_perms = map(int, input().split())
    
    count = 0
    min_prime = max_prime = None
    
    for i in range(2, n_max + 1):
        if is_prime(i):
            perms = find_permutations(i)
            if len([p for p in perms if is_prime(p)]) == k_perms:
                count += 1
                if min_prime is None or i < min_prime:
                    min_prime = i
                if max_prime is None or i > max_prime:
                    max_prime = i
    
    print([count, min_prime, max_prime])

if __name__ == "__main__":
    main()
