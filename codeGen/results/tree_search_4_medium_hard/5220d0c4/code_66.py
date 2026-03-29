import sys

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]

def get_min_prime_divisor(n):
    primes = sieve_of_eratosthenes(n)
    for prime in reversed(primes):
        if n % prime == 0:
            return prime

def is_good_prime(n, bad_primes):
    return not any(bad_prime in (str(n), str(i)) for i in range(2, int(n ** 0.5) + 1))

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    
    dp = [[0] * (max(arr) + 1) for _ in range(n + 1)]
    last_prime = [0] * (n + 1)
    max_beauty = [0] * (n + 1)

    for i in range(1, n + 1):
        min_prime_divisor = get_min_prime_divisor(arr[i - 1])
        is_good = is_good_prime(min_prime_divisor, bad_primes)
        
        if dp[i - 1][min_prime_divisor]:
            max_beauty[i] = max(max_beauty[:i], [dp[j][last_prime[j]] for j in range(i)] + [max_beauty[j] for j in range(i)])
            last_prime[i] = min_prime_divisor
        else:
            max_beauty[i] = 0

    print(max(max_beauty))

if __name__ == "__main__":
    solve()
