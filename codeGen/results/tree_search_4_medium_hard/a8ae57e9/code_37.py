import sys

def solve():
    n, k = map(int, input().split())
    pi = list(map(int, input().split()))
    ri = [0] + list(map(int, input().split()))

    dp = [[0] * (sum(pi) + 1) for _ in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, sum(pi) + 1):
            max_earnings = 0
            for request in range(n):
                if ri[request] <= i and j >= pi[request]:
                    new_earnings = dp[i - ri[request]][j - pi[request]] + pi[request]
                    if new_earnings > max_earnings:
                        max_earnings = new_earnings
            dp[i][j] = max(0, max_earnings)

    accepted_requests = 0
    total_amount = dp[k][sum(pi)]
    for i in range(k, -1, -1):
        for j in range(sum(pi), -1, -1):
            if dp[i][j] > dp[i][j-1]:
                accepted_requests += ri[pi.index(j)]
                total_amount -= j
                break

    print(total_amount)
    print(accepted_requests)

for _ in range(int(input())):
    solve()
