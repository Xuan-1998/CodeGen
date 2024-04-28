n = int(input())
sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + int(input())

left_sum = sums[n]
right_sum = 0
max_partitions = 0

i = 0
while i < n:
    if left_sum == right_sum:
        max_partitions += 1
        left_sum -= sums[i]
        right_sum = 0
        i = 0
    elif left_sum > right_sum:
        right_sum += sums[i]
    else:
        left_sum -= sums[i]
    i += 1

print(max_partitions)
