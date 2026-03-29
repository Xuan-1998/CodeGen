import sys

def generate_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

def prime_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    def permute(arr, l, r):
        if l == r:
            permutation = int(''.join(map(str, arr)))
            if is_prime(permutation):
                permutations.add(permutation)
        else:
            for i in range(l, r + 1):
                arr[l], arr[i] = arr[i], arr[l]
                permute(arr, l + 1, r)
                arr[l], arr[i] = arr[i], arr[l]

    permute(digits, 0, len(digits) - 1)
    return permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max, k_perms = map(int, sys.stdin.readline().split())
primes = generate_primes(n_max)
prime_count = 0
smallest = float('inf')
largest = -float('inf')

for prime in primes:
    if len(prime_permutations(prime)) == k_perms:
        prime_count += 1
        smallest = min(smallest, prime)
        largest = max(largest, prime)

print([prime_count, smallest, largest])
