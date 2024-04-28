def solve():
    n = int(input())
    a, b = [int(x) for x in input().split()]
    
    dp = [[0] * 20 for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(20):
            if (a & (1 << j)) == 0 or (b >> i) & (1 << j):
                break
            dp[i][j] = ((dp[i - 1][j] + a) if i > 0 else a) % (10**9 + 7)
    
    ans = sum(dp[i][-1] for i in range(n + 1))
    print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
