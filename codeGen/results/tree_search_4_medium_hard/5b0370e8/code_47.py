def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for s in range(1 << k):
                if s & (s - 1):  # If the last bit is set
                    for j in range(k):
                        if not (s & (1 << j)):
                            dp[i][s] += dp[i - 1][(s ^ (1 << j))]
                else:  # If the last bit is not set
                    dp[i][s] = dp[i - 1][s]
        print(sum(dp[-1]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
