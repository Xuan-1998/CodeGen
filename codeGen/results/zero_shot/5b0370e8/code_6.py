import sys

def solve():
    t = int(input())
    mod = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n + 1)]
        
        for i in range(2 ** k):
            dp[0][i] = 1
        
        for i in range(1, n + 1):
            for j in range(2 ** k):
                if not any((j & (1 << bit)) > 0 for bit in range(k)):
                    dp[i][j] += sum(dp[i - 1][mask] for mask in range(j + 1))
        
        and_count = sum(dp[n][i] for i in range(2 ** k) if i >= (1 << (k - 1)))
        xor_count = sum(dp[n][i] for i in range(2 ** k))
        result = (and_count - xor_count) % mod
        
        print(result)

if __name__ == "__main__":
    solve()
