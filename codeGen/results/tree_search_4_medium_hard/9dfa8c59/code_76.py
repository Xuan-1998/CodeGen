import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    def permute(index):
        if index >= len(digits):
            permutation = int(''.join(map(str, digits)))
            if is_prime(permutation):
                permutations.add(permutation)
        else:
            for i in range(index, len(digits)):
                digits[index], digits[i] = digits[i], digits[index]
                permute(index + 1)
                digits[index], digits[i] = digits[i], digits[index]
    permute(0)
    return len([x for x in permutations if is_prime(x)])

def solve(n_max, k_perms):
    dp = [[0] * (k_perms + 1) for _ in range(n_max + 1)]
    primes = [True] * (n_max + 1)
    for i in range(2, int(n_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False
    for p in range(2, n_max + 1):
        if primes[p]:
            dp[p][0] = 1
            for k in range(1, min(p, k_perms) + 1):
                if is_prime(int(''.join(map(str, sorted(str(p))))) - p and count_permutations(p) == k:
                    dp[p][k] += 1
    return [dp[n_max][k_perms], 0 if not dp else min([p for p in range(2, n_max + 1) if primes[p] and dp[p][k_perms]], default=0), 
            max([p for p in range(2, n_max + 1) if primes[p] and dp[p][k_perms]], default=0)]

# Read input from stdin
n_max, k_perms = map(int, input().split())

# Print the solution to stdout
print(*solve(n_max, k_perms))
