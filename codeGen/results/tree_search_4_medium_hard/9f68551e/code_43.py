import sys

def solve():
    t = int(input())
    dp = [[0] * (10001) for _ in range(101)]

    for _ in range(t):
        n = int(input())
        k = list(map(int, input().split()))
        h = list(map(int, input().split()))

        for i in range(n+1):
            dp[i][n-i] = float('inf')

        for i in range(n-1, -1, -1):
            for j in range(i+1):
                if k[j] <= i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = dp[i-1][j]

        print(min(dp[n]))

if __name__ == "__main__":
    solve()
