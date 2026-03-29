n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

strings.sort(key=lambda s: (-costs[0], s))

total_cost = 0
for i in range(1, n):
    if strings[i] != strings[i-1]:
        total_cost += costs[i]

print(total_cost)
