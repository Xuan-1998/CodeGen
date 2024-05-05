n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

sorted_strings = sorted(strings)
reversed_costs = [(costs[i], cost) for i, cost in enumerate(costs)]

min_cost = float('inf')
for i in range(n):
    for j in range(i+1, n):
        if sorted_strings[i] < sorted_strings[j]:
            min_cost = min(min_cost, reversed_costs[i][0] + reversed_costs[j][0])

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
