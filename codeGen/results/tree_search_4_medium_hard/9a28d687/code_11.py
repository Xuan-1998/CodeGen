from collections import defaultdict

def min_cost_to_sort(n, costs, strings):
    dp = {(i, False): 0 for i in range(n)}
    for i in range(1, n):
        for rev in [False, True]:
            if rev:
                cost = costs[i]
                if strings[i-1] > strings[i]:
                    cost += costs[i-1]
                else:
                    dp[(i, rev)] = min(dp.get((i-1, False), float('inf')) + costs[i], dp.get((i-1, True), float('inf')) + 2*costs[i])
            else:
                if strings[i-1] > strings[i]:
                    cost += costs[i]
                else:
                    dp[(i, rev)] = min(dp.get((i-1, False), float('inf')) + costs[i], dp.get((i-1, True), float('inf')) + 2*costs[i])
    return dp.get((n-1, False), -1)

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

print(min_cost_to_sort(n, costs, strings))
