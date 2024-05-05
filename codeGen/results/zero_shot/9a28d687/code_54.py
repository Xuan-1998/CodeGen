import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

total_cost = 0

for i in range(n):
    rev_cost = costs[i]
    if strings[i][::-1] < strings[0]:
        strings.insert(0, strings.pop(i))
        total_cost += rev_cost
    elif all(strings[j][::-1] > strings[i][::-1] for j in range(n)):
        strings.append(strings.pop(i))
        total_cost += rev_cost
    else:
        print(-1)
        sys.exit()

print(total_cost)
