from functools import lru_cache

def solve(n):
    @lru_cache(None)
    def has_consecutive_ones(k):
        while k:
            if k & 1 and (k & 2) or (k & 4):
                return True
            k >>= 1
        return False

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if not has_consecutive_ones(i):
            dp[i] = 2 * dp[i - 1]
        else:
            dp[i] = dp[i - 1]

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
