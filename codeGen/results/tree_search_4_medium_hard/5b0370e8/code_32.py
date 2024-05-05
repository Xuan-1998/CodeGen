===BEGIN SOLUTION===
def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        xor_sum = 0
        for i in range(n):
            x, = map(int, input().split())
            xor_sum ^= x
        for i in range(n + 1):
            for j in range(k + 1):
                if i == 0:
                    dp[i][j] = 1
                else:
                    if j > 0:
                        dp[i][j] = (dp[i-1][j-1] * (2**k - 2**(k-j)) + dp[i-1][j]) % (10**9 + 7)
                    dp[i][j] += xor_sum < 2**k - 2**(k-j) and xor_sum >= 2**(k-j) - 1
                    dp[i][j] %= (10**9 + 7)
        print(dp[n][k])
solve()
===END SOLUTION===
