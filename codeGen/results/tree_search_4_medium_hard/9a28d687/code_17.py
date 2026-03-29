def min_cost_to_sort_strings(costs, strings):
    n = len(strings)
    memo = {}

    def dp(i, prev_str, rev):
        if (i, prev_str, rev) in memo:
            return memo[(i, prev_str, rev)]

        if i == n:
            return 0

        total_cost = float('inf')
        for j in range(i + 1):
            new_prev_str = strings[j] if not rev else strings[j][::-1]
            if strings[j].startswith(new_prev_str):
                cost = costs[i] + dp(j, new_prev_str, True)
                total_cost = min(total_cost, cost)

        memo[(i, prev_str, rev)] = -1 if total_cost == float('inf') else total_cost
        return memo[(i, prev_str, rev)]

    total_cost = dp(0, '', False)
    return -1 if total_cost == float('inf') else total_cost


n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

print(min_cost_to_sort_strings(costs, strings))
