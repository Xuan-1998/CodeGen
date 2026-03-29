import sys

n = int(input())
costs = [0] * n
strings = []
for i in range(n):
    costs[i], s = map(str, input().split())
    strings.append((s, int(costs[i])))

strings.sort()

min_cost = 0
prev_string = ""
for string, cost in strings:
    if string < prev_string:
        min_cost += cost
    else:
        for i in range(n):
            if strings[i][0] == string:
                min_cost += costs[i]
                break
    prev_string = string

print(min_cost)
