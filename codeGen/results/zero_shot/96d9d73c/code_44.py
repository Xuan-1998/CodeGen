import sys

# Your existing codes here...

partition_count = 0
current_partition_size = 0
for num in a:
    if current_partition_size + 1 >= k or abs(num - a[0]) > m:
        partition_count += 1
        current_partition_size = 1
    else:
        current_partition_size += 1

print(partition_count <= (n - k + 1))
