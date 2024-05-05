from sys import stdin

n, k = map(int, stdin.readline().split())
requests = [list(map(int, stdin.readline().split())) for _ in range(n)]
requests.sort()

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if requests[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        elif requests[i-1][1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-requests[i-1][0]] + requests[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(f"{dp[-1][-1]} {sum(request[1] for request in requests)}")

for i, request in enumerate(requests):
    if request[1] <= k:
        print(i+1, request[0])
