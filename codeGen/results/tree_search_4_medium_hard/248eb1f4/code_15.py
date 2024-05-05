def solve():
    t = int(input())
    for _ in range(t):
        m, x = map(int, input().split())
        dp = [-1] * (x + 1)
        dp[0] = 0
        for i in range(1, x + 1):
            if i < m:
                dp[i] = (i + 1) % (x + 1)
            else:
                dp[i] = (dp[(i - m) % (x + 1)] + 1) % (x + 1)
        for i in range(1, x + 1):
            print(dp[i], end=' ')
        print()

if __name__ == "__main__":
    solve()
