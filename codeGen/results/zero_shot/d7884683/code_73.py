t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        print(0)
    else:
        max_partitions = 0
        left_sum = total_sum // 2
        current_left_sum = 0
        for i in range(n):
            current_left_sum += arr[i]
            if current_left_sum == left_sum:
                max_partitions += 1
                current_left_sum = 0
        print(max_partitions)
