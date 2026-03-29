import sys

def solve(n, k, tables):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if tables[j - 1] >= i:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + requests[i - 1][0] * requests[i - 1][1])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
    ans = [0, 0]
    for i in range(n, 0, -1):
        if dp[i][k] > dp[i - 1][k]:
            ans = [i, requests[i - 1][0], k]
            break
    return *ans

n, k, tables = map(int, input().split())
requests = []
for _ in range(n):
    size, amount = map(int, input().split())
    requests.append((size, amount))
print(*solve(n, k, tables), sep='\n')
