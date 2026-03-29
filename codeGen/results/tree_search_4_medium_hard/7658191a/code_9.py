import sys

def solve():
    n, k, z = map(int, input().split())
    a = list(map(int, input().split()))
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = a[i - 1]
            else:
                left = right = 0
                if j <= z and i > 1:
                    left = dp[i - 2][j - 1] + a[i - 1]
                if i < n:
                    right = dp[i + 1][j - 1] + a[i]
                dp[i][j] = max(left, right)
    
    print(dp[n][k])

if __name__ == "__main__":
    solve()
