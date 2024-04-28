from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = defaultdict(int)
    dp[0, 0] = 0

    max_partitions = 0
    for i in range(n):
        left_sum = prefix_sum[i]
        right_sum = prefix_sum[n] - left_sum
        if right_sum == left_sum:
            num_partitions = (i // 2) + 1 if i % 2 == 0 else i // 2
            dp[left_sum, num_partitions] = max(num_partitions, dp.get(left_sum, 0))
            max_partitions = max(max_partitions, dp[left_sum, num_partitions])

    return max_partitions


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
