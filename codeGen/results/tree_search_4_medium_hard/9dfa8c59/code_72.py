import sys
from itertools import permutations

def get_prime_permutations(n):
    prime_perms = set()
    for p in range(2, n+1):
        if is_prime(p):
            perms = set(''.join(map(str, p)))
            if len(perms) == k_perms:
                prime_perms.add(p)
    return prime_perms

def main():
    global k_perms
    n_max, k_perms = map(int, sys.stdin.readline().split())
    prime_perms = get_prime_permutations(n_max)
    count = len(prime_perms)
    if count > 0:
        min_prime = min(prime_perms)
        max_prime = max(prime_perms)
        print(count, min_prime, max_prime)
    else:
        print(0, 0, 0)

def is_prime(n):
    if n <= 1:
        return False
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return False
    return True

if __name__ == "__main__":
    main()
