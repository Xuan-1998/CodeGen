from collections import defaultdict

def partition_max_times():
    t = int(input())
    memo = defaultdict(int)

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        total_sum = sum(arr)
        max_partitions = 0

        left_sum = 0
        for right_sum in range(total_sum + 1):
            if (n - 1, left_sum) in memo:
                right_partition = memo[(n - 1, left_sum)] + (right_sum != total_sum // 2)
                max_partitions = max(max_partitions, right_partition)

            if left_sum == right_sum:
                max_partitions = max(max_partitions, 1)

            left_sum += arr[0]
            arr.pop(0)

        print(max_partitions)

partition_max_times()
