import sys
from functools import lru_cache

def solve():
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    @lru_cache(None)
    def dp(i):
        if i > C:
            return 0
        return sum((U.count(j) for j in range(1, i+1))) * binomial(N, i) + sum((L.count(j) for j in range(C-i+1, C+1))) * binomial(M, C-i)

    print(sum(dp(i) % (10**9+7) for i in range(1, C+1)))

def binomial(n, k):
    if k > n // 2:
        k = n - k
    a, b = 1, 1
    for i in range(k):
        a *= n - i
        b *= i + 1
    return a // b

if __name__ == "__main__":
    solve()
