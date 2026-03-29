import sys

def solve(n, a):
    mod = 10**9 + 7
    dp = [[0] * (max(a) + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(max(a), 0, -1):
            if i >= a[j-1]:
                if a[i-1] % j == 0:
                    dp[i][j] = (dp[i-1][j] + 1) % mod
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][max(a)] % mod

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
