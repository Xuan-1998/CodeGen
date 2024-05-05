import sys
from functools import lru_cache

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    dp = [False] * (n + 1)
    dp[0] = True

    @lru_cache(None)
    def dfs(i):
        if not dp[i]:
            return False
        for j in range(1, i):
            if (values[j - 1] ^ values[i - 1]) == (values[i // 2] if i % 2 else 0):
                dp[i] = dp[j] and dfs(j)
                break
        return dp[i]

    print("YES" if dfs(n) else "NO")

if __name__ == "__main__":
    solve()
