import sys

def find_primes():
    n_max, k_perms = map(int, input().split())
    
    memo = {}
    primes = set()

    def is_prime(n):
        if n in memo:
            return memo[n]
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1): 
            if n % i == 0: 
                memo[n] = False
                return False
        memo[n] = True
        return True

    def count_permutations(n):
        perms = set()
        for p in str(n):
            p = int(p)
            perms.add(tuple(sorted([p, *map(int, str(n).replace(str(p), ''))])))
        return len([*filter(lambda x: is_prime(int(''.join(map(str, x)))), perms)])

    count = 0
    smallest = float('inf')
    largest = -float('inf')

    for n in range(2, n_max + 1):
        if is_prime(n):
            c = count_permutations(n)
            if c == k_perms:
                count += 1
                smallest = min(smallest, n)
                largest = max(largest, n)

    print([count, smallest, largest])

if __name__ == "__main__":
    find_primes()
