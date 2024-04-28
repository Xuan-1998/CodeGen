from collections import defaultdict
def partition_array():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        memo = defaultdict(dict)
        max_partition = 0
        for i in range(n):
            right_sum = sum(arr[i:])
            left_sum = sum(arr[:i])
            diff_sum = abs(left_sum - right_sum)
            if (i, right_sum) not in memo:
                memo[(i, right_sum)] = diff_sum
            else:
                max_partition += 1
        print(max_partition)

partition_array()
