import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    digits = [int(digit) for digit in str(n)]
    permutations = set()
    for p in itertools.permutations(digits):
        permutation = int(''.join(map(str, p)))
        if permutation < n and is_prime(permutation):
            permutations.add(permutation)
    return len(permutations)

def solve():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    prime_counts = {}
    for i in range(2, n_max + 1):
        if is_prime(i):
            prime_counts[i] = count_permutations(i)

    result_count = 0
    smallest_prime = largest_prime = 0
    for prime, count in prime_counts.items():
        if count == k_perms:
            result_count += 1
            if not smallest_prime or prime < smallest_prime:
                smallest_prime = prime
            if not largest_prime or prime > largest_prime:
                largest_prime = prime

    print([result_count, smallest_prime, largest_prime])

if __name__ == '__main__':
    solve()
