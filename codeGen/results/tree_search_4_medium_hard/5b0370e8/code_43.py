from functools import lru_cache

def solve():
    t = int(input())
    MOD = 10**9 + 7
    dp = [[0] * (1 << k) for _ in range(n+1)]
    
    @lru_cache(None)
    def dfs(i, mask):
        if i == n:
            return 1
        res = 0
        for j in range(k-1, -1, -1):
            last_bit = (mask >> j) & 1
            res += dp[i][last_bit]
            res %= MOD
        return res
    
    for _ in range(t):
        n, k = map(int, input().split())
        result = dfs(n, 0)
        print(result)

if __name__ == "__main__":
    solve()
