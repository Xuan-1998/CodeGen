import sys

def solve():
    n, k, m = map(int, input().split())
    requests = []
    for _ in range(n):
        group_size, amount = map(int, input().split())
        requests.append((group_size, amount))

    dp = [[0] * (m + 1) for _ in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, m + 1):
            if i > 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][max(0, j-group_size)] + group_size * amount)
            else:
                dp[i][j] = min(j, group_size) * amount

    accepted_requests = 0
    total_amount = 0
    table_assignment = []
    for i in range(k, -1, -1):
        for j in range(m, -1, -1):
            if dp[i][j] != dp[i-1][j]:
                accepted_requests += 1
                total_amount += min(j, requests[accepted_requests-1][0]) * requests[accepted_requests-1][1]
                table_assignment.append((accepted_requests, i))

    print(accepted_requests, total_amount)
    for request, table in table_assignment:
        print(request, table)

if __name__ == "__main__":
    solve()
