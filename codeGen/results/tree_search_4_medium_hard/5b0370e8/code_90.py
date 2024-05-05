def solve():
    t = int(input())
    MOD = 10**9 + 7
    dp = [[0] * (2**20) for _ in range(21)]
    
    def andor(i, k):
        if i >= 2**k: return 1
        res = 1
        for j in range(k-1, -1, -1):
            if i & (1 << j): res += dp[j][i^(1<<j)] * andor(i^(1<<j), j)
            else: res += andor(i, j) * andor(i|(1<<j), k-j-1)
        return res % MOD
    
    for _ in range(t):
        n, k = map(int, input().split())
        ans = andor(2**k - 1, k)
        print(ans)

if __name__ == "__main__":
    solve()
