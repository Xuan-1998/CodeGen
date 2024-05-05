from collections import defaultdict
import heapq

def beauty(arr, bad_primes):
    memo = defaultdict(int)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        res = 0
        while i > 0 and j < len(bad_primes):
            res += max(dp(i-1, j), gcd(arr[i], bad_primes[j]))
            i -= 1
            j += 1

        if not (i > 0 or j < len(bad_primes)):
            res = f(gcd(*arr))

        memo[(i, j)] = res
        return res

    def f(s):
        p = min(prime_divisors(s))
        return s - s // p if p in bad_primes else s + s // p

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def prime_divisors(n):
        i = 2
        divs = []
        while i * i <= n:
            if n % i:
                j = i
                while j * i <= n and n % (j * i):
                    j *= i
                divs.append(j)
                n //= j
            else:
                n //= i
            i += 1
        if n > 1:
            divs.append(n)
        return divs

    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    res = dp(len(arr), 0)
    return res
