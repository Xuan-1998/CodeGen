def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    prev_min_cost = [float('inf')] * (n + 1)

    for i in range(1, n + 1):
        min_cost = float('inf')
        last_string = strings[i - 1]
        for j in range(i):
            if last_string < strings[j]:
                cost = costs[j] + prev_min_cost[j]
                if cost < min_cost:
                    min_cost = cost
        dp[i][i] = min_cost

    total_cost = float('inf')
    for k in range(1, n + 1):
        total_cost = min(total_cost, dp[n][k])
    if total_cost == float('inf'):
        print(-1)
    else:
        print(total_cost)

solve()
