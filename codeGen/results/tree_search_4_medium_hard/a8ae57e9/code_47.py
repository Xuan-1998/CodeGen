import sys

n, k = map(int, input().split())
dp = [[0] * (1001) for _ in range(1002)]
for i in range(k + 1):
    dp[i][0] = 0

for i in range(k + 1):
    for j in range(1001):
        if i > 0 and j >= k:
            break
        if j == 0:
            continue
        for request in sys.stdin:
            group_size, money_spent = map(int, request.split())
            if group_size <= i and money_spent <= j:
                dp[i][j] = max(dp[i-1][group_size] + (money_spent - group_size * 5), dp[i][j-1])
        if i > 0:
            for _ in range(i):
                print(f"accept {request.split()[1]} at table {_+1}", file=sys.stderr)

print(f"{sum(1 for request in sys.stdin if int(request.split()[1]) <= k)} {dp[k][n]}")

