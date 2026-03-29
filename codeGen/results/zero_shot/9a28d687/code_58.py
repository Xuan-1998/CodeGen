n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

total_cost = 0

for i in range(n):
    if any(strings[i] < s for s in strings[:i]):
        total_cost += costs[i]
    else:
        break
else:
    print(-1)
print(total_cost)
