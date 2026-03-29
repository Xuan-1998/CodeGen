import heapq

def get_prime_divisors(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    primes = []
    i = 2
    while i * i <= n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def get_beauty(arr, bad_primes):
    beauty = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        good_primes = []
        for j in range(i+1):
            if arr[j] not in bad_primes:
                good_primes.append(arr[j])
        heapq.heapify(good_primes)
        beauty[i+1] = len(good_primes) + (0 if good_primes else 1)
    return beauty

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    primes = get_prime_divisors(max(arr))
    bad_primes = [p for p in bad_primes if p in primes]
    beauty = get_beauty(arr, bad_primes)

    print(beauty[-1])

solve()
