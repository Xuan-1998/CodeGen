import heapq

def max_beauty(n, m, arr, bad_primes):
    memo = {}

    def dfs(i):
        if i >= n:
            return 0
        if (i,) in memo:
            return memo[(i,)]
        res = 0
        for j in range(i+1, n+1):
            p = min_prime_divisor(arr[j-1])
            if p not in bad_primes and p == min_prime_divisor(arr[i:j]):
                res += dfs(j)
        return res

    def min_prime_divisor(x):
        for i in range(2, int(x**0.5) + 1):
            if x % i:
                continue
            if i * i != x:
                return i
            break
        return x

    return dfs(0)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
