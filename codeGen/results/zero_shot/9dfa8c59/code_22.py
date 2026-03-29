import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n):
    permutations = set()
    def permute(digits, current):
        if not digits:
            permutations.add(int(current))
        else:
            for i in range(len(digits)):
                digit = int(digits[i])
                remaining_digits = digits[:i] + digits[i+1:]
                permute(remaining_digits, str(digit) + current)
    permute(str(n), '')
    return [x for x in permutations if is_prime(x)]

def solve():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    primes_with_k_perms = prime_permutations(n_max)
    count = len(primes_with_k_perms)
    smallest = largest = None
    if count:
        smallest = min(primes_with_k_perms)
        largest = max(primes_with_k_perms)
    print([count, smallest or 0, largest or 0])

if __name__ == "__main__":
    solve()
