def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << (k-1)) for _ in range(n+1)]
        for j in range(2**(k-1)):
            if bin(j)[2:].zfill(k-1).count('1') % 2 == 0:
                for i in range((n+1)*2**(k-1)-1, -1, -1):
                    dp[i][j] = (dp[max(0, i-(2**k)-1)][j] + dp[min(n, i)][j]) % (10**9+7)
            else:
                for i in range((n+1)*2**(k-1)-1, -1, -1):
                    dp[i][j] = (dp[max(0, i-(2**k)-1)][j] + 1) % (10**9+7)
        print(sum(dp[n]) % (10**9+7))

if __name__ == "__main__":
    solve()
