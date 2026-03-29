import sys

def solve(n, M):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1):
            if M[j-1] == i:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD

    return sum(dp[n])

if __name__ == '__main__':
    n = int(input())
    M = list(map(int, input().split()))
    print(solve(n, M))
