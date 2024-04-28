n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    left_sum = 0
    partitions = 0
    for i in range(len(arr)):
        if left_sum == total_sum - left_sum:
            partitions += 1
            left_sum = 0
        left_sum += arr[i]
    print(partitions)
