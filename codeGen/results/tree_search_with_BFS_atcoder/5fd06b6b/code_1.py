n = int(input())
counts = list(map(int, input().split()))

counts.reverse()

max_count = 0
sum_counts = 0

for c in counts:
    if c < max_count:
        sum_counts += c
    else:
        sum_counts += max_count
        max_count = c

print(sum_counts)

