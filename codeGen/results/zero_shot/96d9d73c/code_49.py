import sys

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

partitions = 1
current_partition_sum = a[0]

for i in range(1, n):
    if a[i] - current_partition_sum > m:
        partitions += 1
        current_partition_sum = a[i]
    else:
        current_partition_sum += a[i]

print(partitions >= k)
