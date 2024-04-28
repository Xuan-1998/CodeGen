from collections import defaultdict

def partition_times():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        memo = defaultdict(lambda: [-1, 0])
        max_partitions = 0
        curr_sum = 0
        for i, x in enumerate(arr):
            if memo[i][0] == -1:
                left_sum = sum(arr[:i+1])
                right_sum = sum(arr[i:])
                if left_sum == right_sum:
                    partitions = (i // 2) + 1
                    max_partitions = max(max_partitions, partitions)
            curr_sum += x
            if curr_sum * 2 > sum(arr):
                break
        print(max_partitions)

partition_times()
