from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = defaultdict(int)
    res = 0

    for i in range(1, n // 2 + 1):
        left_sum = prefix_sum[i]
        right_sum = prefix_sum[n] - left_sum
        if (left_sum, right_sum) in dp:
            res = max(res, dp[(left_sum, right_sum)] + 1)
        dp[(left_sum, right_sum)] = i

    return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
