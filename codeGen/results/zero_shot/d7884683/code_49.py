n = int(input())
arr = list(map(int, input().split()))
left_sum = 0
max_partition_count = 0
for i in range(len(arr)):
    left_sum += arr[i]
    right_sum = sum(arr[:i])
    if left_sum == right_sum:
        max_partition_count = i // 2 + (i % 2)
        break
print(max_partition_count)
