strings.sort()
min_cost = 0

for i in range(n):
    if strings[i] == sorted_strings[i]:
        continue
    else:
        for j in range(i+1, n):
            if len(sorted_strings[j]) < len(strings[i]):
                break
        min_cost += costs[j]
        costs[j] = -1  # mark as processed

print(min_cost)
