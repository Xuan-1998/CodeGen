import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        count = 0
        for i in range(1, n + 1):
            last_bit = int(input()) & ((1 << k) - 1)
            for j in range(k, -1, -1):
                if (last_bit >> j) & 1:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += dp[i - 1][k - j]
            count = (count + dp[i][0]) % (10**9 + 7)
        print(count)

if __name__ == '__main__':
    solve()
