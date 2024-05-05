import sys

def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    requests = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][min(j, requests[i - 1][0])] + requests[i - 1][1])
    
    total_earned = dp[n][k]
    accepted_requests = sum(1 for i in range(n) if dp[i][k] == dp[i - 1][k] + requests[i][1])

    print(total_earned, accepted_requests)

    table = k
    total_amount = 0

    for i in range(n, 0, -1):
        if dp[i][table] > dp[i - 1][table]:
            print(i, table)
            total_amount += requests[i - 1][1]
            table -= requests[i - 1][0]
        else:
            break
    
    print(total_amount)

if __name__ == "__main__":
    solve()
