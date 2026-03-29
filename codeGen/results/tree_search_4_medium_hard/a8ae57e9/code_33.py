def solve(n, k, requests):
    dp = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, k+1):
        dp[i][0] = 0

    for j in range(1, n+1):
        ri, pi = requests[j-1]
        for used_tables in range(1, k+1):
            dp[used_tables][j] = max(dp[used_tables-1][j-ri*pi] + ri*pi, dp[used_tables][j])

    return dp[k][n]

if __name__ == '__main__':
    n, k = map(int, input().split())
    requests = []
    for _ in range(n):
        requests.append(list(map(int, input().split())))

    print(*solve(n, k, requests))
