import sys

def solve():
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(m+1):
        if i <= 0:
            continue
        for j in range(1, min(i+1, m+1)):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-arr[j-1]][j-1] + dp[i][j-1]) % (10**9+7)

    print(dp[n][m])

if __name__ == "__main__":
    solve()
