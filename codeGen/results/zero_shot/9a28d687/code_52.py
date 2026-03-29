n = int(input())
costs = [0] * n
strings = []

for i in range(n):
    cost = int(input())
    costs[i] = cost
    strings.append(input().strip())

strings.sort(key=lambda s: (-len(s), s))

total_cost = 0
for i in range(n):
    prev_len = len(strings[i])
    while i > 0 and len(strings[i-1]) >= prev_len:
        strings[i] = strings[i][::-1]
        total_cost += costs[i]
        if len(strings[i]) < prev_len:
            break
        i -= 1

if any(len(s) != prev_len for s in strings):
    print(-1)
else:
    print(total_cost)
