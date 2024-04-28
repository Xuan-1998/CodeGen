n = int(input())
sum_left = 0
max_partitions = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    sum_total = sum(arr)
    if sum_total % 2 != 0:
        continue
    total_sum = sum_total // 2
    partitions = 0
    left_sum = 0
    for i, num in enumerate(arr):
        left_sum += num
        if left_sum == total_sum:
            partitions += 1
            left_sum = 0
    max_partitions = max(max_partitions, partitions)
print(max_partitions)
