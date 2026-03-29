from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(digits):
    perms = set(int(''.join(map(str, p))) for p in permutations(digits))
    return sum(1 for perm in perms if is_prime(perm))

def solve():
    n_max, k_perms = map(int, input().split())
    prime_count = 0
    smallest = float('inf')
    largest = -float('inf')

    memo = {}
    for i in range(2, n_max + 1):
        if is_prime(i):
            digits = str(i)
            if digits not in memo:
                memo[digits] = count_permutations(digits)
            k_perms_count = memo[digits]
            if k_perms_count == k_perms:
                prime_count += 1
                smallest = min(smallest, i)
                largest = max(largest, i)

    print([prime_count, smallest, largest])

solve()
