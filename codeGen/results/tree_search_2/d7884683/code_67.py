from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    memo = defaultdict(int)

    def dp(left_sum, right_sum):
        if (left_sum, right_sum) in memo:
            return memo[(left_sum, right_sum)]
        if left_sum == 0 and right_sum == sum(arr):
            return 1
        max_partitions = 1
        for i in range(1, n // 2 + 1):
            left_sum_new = left_sum - arr[i-1]
            right_sum_new = right_sum - arr[-i]
            if left_sum_new >= 0 and right_sum_new >= 0:
                max_partitions = max(max_partitions, dp(left_sum_new, right_sum_new) + 1)
        memo[(left_sum, right_sum)] = max_partitions
        return max_partitions

    total_sum = sum(arr)
    max_partitions = 0
    for i in range(1, n // 2 + 1):
        left_sum = total_sum - arr[i-1]
        right_sum = arr[i-1]
        max_partitions = max(max_partitions, dp(left_sum, right_sum))
    return max_partitions

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
