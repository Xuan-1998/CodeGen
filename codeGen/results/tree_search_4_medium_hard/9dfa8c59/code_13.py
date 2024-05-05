import sys
from collections import defaultdict

def generate_permutations(num):
    num_str = str(num)
    permutations = set()
    for i in range(len(num_str)):
        remaining_digits = num_str[:i] + num_str[i+1:]
        if remaining_digits:
            for p in generate_permutations(int(remaining_digits)):
                permutations.add(int(num_str[0] + str(p)))
        else:
            permutations.add(int(num_str[0]))
    return permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solve():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    prime_count_dict = defaultdict(int)
    seen_primes = set()
    
    for num in range(2, n_max + 1):
        if is_prime(num):
            permutations = generate_permutations(num)
            seen_primes.add(num)
            prime_count_dict[num] = len([p for p in permutations if is_prime(p) and p in seen_primes])
    
    total_count = sum(1 for count in prime_count_dict.values() if count == k_perms)
    smallest_prime = min((num for num, count in prime_count_dict.items() if count == k_perms))
    largest_prime = max((num for num, count in prime_count_dict.items() if count == k_perms))
    
    print([total_count, smallest_prime, largest_prime])

if __name__ == "__main__":
    solve()
