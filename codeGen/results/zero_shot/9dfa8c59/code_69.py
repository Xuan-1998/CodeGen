import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

def prime_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = []
    def permute(a, l):
        if len(a) > l:
            return
        for i in range(len(a)):
            remainder = a[i:]
            yield int(''.join(map(str, [digits[0]] + remainder))), *permute(remainder, l+1)
    result = set()
    for p in permute(digits, 0):
        if len(str(p)) > len(str(n)):
            continue
        if str(p) == str(n):
            continue
        if int(str(p)[0]) != digits[0]:
            continue
        if p not in result:
            result.add(p)
    return len(result)

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

prime_numbers = sieve_of_eratosthenes(n_max)

count = 0
smallest = float('inf')
largest = float('-inf')

for n in prime_numbers:
    if prime_permutations(n) == k_perms:
        count += 1
        smallest = min(smallest, n)
        largest = max(largest, n)

print([count, smallest, largest])
