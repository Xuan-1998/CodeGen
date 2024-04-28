n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    left_sum = 0
    max_partitions = 0
    for i in range(len(arr)):
        left_sum += arr[i]
        if left_sum == (total_sum - left_sum) // 2:
            max_partitions += 1
    print(max_partitions)
