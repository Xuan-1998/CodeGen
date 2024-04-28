t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    left_sum = 0
    max_partitions = 0
    for i in range(n):
        if left_sum == (total_sum - left_sum) // 2:
            max_partitions += 1
        left_sum += arr[i]
    print(max_partitions)
