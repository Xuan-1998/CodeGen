from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    memo = defaultdict(int)

    def dp(index, partition_count):
        if index >= n:
            return partition_count
        if (index, partition_count) in memo:
            return memo[(index, partition_count)]

        left_sum = prefix_sum[index]
        right_sum = prefix_sum[n] - left_sum

        if left_sum == right_sum:
            partition_count += 1
            new_index = index + 1
        else:
            new_index = index

        result = dp(new_index, partition_count)
        memo[(index, partition_count)] = result
        return result

    return dp(0, 0)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
