import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        b = list(map(int, sys.stdin.readline().split()))
        dp = [[float('inf')] * 2 for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i][0] = min(dp[j][1] + (abs(b[i - 1] - b[i]) or 1) for j in range(i) if j % 2 != 0)
            else:
                dp[i][1] = min(dp[j][0] + (abs(b[i - 1] - b[i]) or 1) for j in range(i) if j % 2 == 0)
        if dp[n][0] <= n and dp[0][1] <= n:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
