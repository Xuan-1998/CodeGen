from collections import namedtuple

Request = namedtuple('Request', ['size', 'amount'])

def solve():
    n, m, k = map(int, input().split())
    requests = [Request(*map(int, input().split())) for _ in range(n)]
    dp = [[0] * (m+1) for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, m+1):
            accepted_requests = 0
            total_amount = 0

            for request in requests:
                if i >= request.size and j >= request.amount:
                    dp[i][j] = max(dp[i-1][j-request.amount], 0) + request.amount
                    accepted_requests += 1
                    total_amount += request.amount
                    break

            if i == k or j == m:
                break

    print(accepted_requests, total_amount)

for i in range(k+1):
    for j in range(m+1):
        if dp[i][j] > 0:
            accepted_requests = -1
            for request in requests:
                if i >= request.size and j >= request.amount:
                    accepted_requests = request.size
                    break
            print(i, accepted_requests)
