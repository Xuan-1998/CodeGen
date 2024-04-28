from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    nums = [int(x) for x in stdin.read().split()[:n]]

    dp = [[False] * m for _ in range(n+1)]
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(m):
            if j >= nums[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    print(1) if any(dp[n][i]) for i in range(m)] else print(0)

if __name__ == "__main__":
    solve()
