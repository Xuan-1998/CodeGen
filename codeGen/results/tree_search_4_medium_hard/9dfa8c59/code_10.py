import sys
from collections import defaultdict

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(num):
    num_str = str(num)
    permutations = set()
    for p in prime_numbers:
        p_str = str(p)
        if len(p_str) != len(num_str):
            continue
        if sorted(p_str) == sorted(num_str):
            permutations.add(int(''.join(sorted(p_str))))
    return len(permutations)

def solve():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    prime_numbers = set()
    for num in range(2, n_max):
        if is_prime(num):
            prime_numbers.add(num)
    
    permutations_count = defaultdict(int)
    for prime_num in prime_numbers:
        permutations_count[prime_num] = count_permutations(prime_num)

    count = sum(1 for k in permutations_count.values() if k == k_perms)
    smallest_prime = min((num for num, k in permutations_count.items() if k == k_perms))
    largest_prime = max((num for num, k in permutations_count.items() if k == k_perms))

    print([count, smallest_prime, largest_prime])

if __name__ == "__main__":
    solve()
