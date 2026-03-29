from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    tables = [int(input()) for _ in range(k)]
    requests = []
    for _ in range(n):
        size, amount = map(int, input().split())
        requests.append((size, amount))

    dp = [[0] * (sum(tables) + 1) for _ in range(k + 1)]

    memo = defaultdict(int)

    for i in range(1, k + 1):
        for j in range(sum(tables) + 1):
            if j < sum(tables) and any(size > tables[m] for m, size in enumerate(requests)):
                dp[i][j] = dp[i-1][j]
            else:
                for m, (size, amount) in enumerate(requests):
                    if size <= tables[0]:
                        dp[i][j] = max(dp[i-1][j-size*amount], dp[i][j])
                    requests.pop(0)
                    break

    total_earned = dp[k][sum(tables)]
    accepted_requests = []
    for j in range(sum(tables) + 1):
        if total_earned == dp[k][j]:
            while j > sum(tables):
                j -= requests[0][1]
                requests.pop(0)
            accepted_requests.extend(requests)

    print(f"{len(accepted_requests)} {total_earned}")

    for i, request in enumerate(accepted_requests):
        size, amount = request
        table_idx = sum(tables) - amount // tables[0]
        print(i+1, table_idx)

solve()
