import sys
from functools import lru_cache

MOD = 998244353

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    A = [0] + A

    @lru_cache(None)
    def dp(i, j, k):
        if i == 0:
            return 1 if j == k == 0 else 0
        res = dp(i - 1, j - 1, k - 1) * (j if j else 1)
        res += dp(i - 1, j, k - 1) * (j * (j - 1) // 2 if k == 2 and j else j)
        res += dp(i - 1, j, k) * ((A[i - 1] - j + 1) * (A[i - 1] - j) // 2 if k == 0 and A[i - 1] - j > 1 else A[i - 1] - j)
        return res % MOD

    print(sum(dp(N, j, min(j, A[N])) for j in range(N + 1)) % MOD)

if __name__ == "__main__":
    main()

