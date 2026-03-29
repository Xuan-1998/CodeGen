n = int(input().strip())
sequence = list(map(int, input().strip().split()))
sequence.sort()

sum_counts = 0
max_count = 0

for count in sequence:
    max_count = max(max_count, count)
    sum_counts += max_count

print(sum_counts)

