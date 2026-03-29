import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            for j in range(i, -1, -1):
                min_val = sys.maxsize
                for x in range(a[j-1] + 1):
                    y = a[j-1] - x
                    if (x - s) * (y - s) >= 0:
                        dp[i][j] = min(dp[i][j], x * dp[i-1][j-1] + y * dp[i-1][j-2])
                dp[i][j-1] = dp[i][j]
        print(dp[n][0])

if __name__ == "__main__":
    solve()
