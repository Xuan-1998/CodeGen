from functools import lru_cache

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    @lru_cache(None)
    def f(n, prev_reduced):
        if n == 1:
            return 0
        good_primes = [p for p in range(2, n + 1) if not any(p % b == 0 for b in B)]
        min_good_prime = min(good_primes)
        if prev_reduced and min_good_prime > 1:
            return f(n // min_good_prime, True) + n
        elif not prev_reduced and min_good_prime > 1:
            return f(n // min_good_prime, False) - n
        else:
            left = f(n // 2, True)
            right = f(n // 2, False)
            return max(left, right)

    memo = {(n, False): f(n, False) for n in range(1, N + 1)}
    print(max(memo[i] for i in range(N, -1, -1)))

if __name__ == "__main__":
    solve()
