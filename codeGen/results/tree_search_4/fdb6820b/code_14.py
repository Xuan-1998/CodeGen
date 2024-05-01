import sys

def solve():
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [[0]*(N+1) for _ in range(m+1)]

    # Base case: there is one way to form 0 (by not including any elements)
    dp[0][0] = 1

    for i in range(1, m+1):
        for j in range(N+1):
            if j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j-arr[i-1]] + dp[i][i]) % (10**9+7)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[m][N])

if __name__ == "__main__":
    solve()
