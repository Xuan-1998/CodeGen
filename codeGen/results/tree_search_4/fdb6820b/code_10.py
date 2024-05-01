from functools import lru_cache

def solve():
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    @lru_cache(None)
    def dp(N, i):
        if N < 0:
            return 0
        if i == 0 or N == 0:
            return 1
    
        res = 0
        for j in range(i):
            if N - arr[j] >= 0:
                res += dp(N - arr[j], j)
        
        return res % (10**9 + 7)

    print(dp(n, m-1))

if __name__ == "__main__":
    solve()
