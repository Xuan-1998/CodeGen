import sys

def count_ways(n, m):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(1, min(i+1, n)+1):
            if m[j-1] <= i:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][n]

def main():
    n = int(input())
    m = list(map(int, input().split()))
    print(count_ways(n, m))

if __name__ == "__main__":
    main()
