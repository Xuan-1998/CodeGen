n = int(input().strip())
counts = list(map(int, input().split()))
counts.sort()

sum_counts = 0
assigned = []

for count in counts:
    if assigned and assigned[-1] < count:
        assigned.append(assigned[-1] + 1)
    else:
        assigned.append(count)
    sum_counts += assigned[-1]

print(sum_counts)

