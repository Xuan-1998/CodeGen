def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]

def min_prime_divisor(n):
    sieve = sieve_of_eratosthenes(n)
    for p in sieve:
        if n % p == 0:
            return p

def max_beauty(arr, bad_primes):
    n = len(arr)
    dp_table = [[0] * (max(bad_primes) + 1) for _ in range(n + 1)]
    flag = [False] * (n + 1)

    for i in range(1, n + 1):
        j = arr[i - 1]
        if j in bad_primes:
            flag[i] = True
        else:
            flag[i] = False
        dp_table[i][0] = max(dp_table[i - 1][:], key=lambda x: (min_prime_divisor(x), flag[x]))

    return max(dp_table[-1])

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(arr, bad_primes))
