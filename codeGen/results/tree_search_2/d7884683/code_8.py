from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    memo = defaultdict(int)

    def dp(i):
        if i == 0: return 1
        if i < 0: return 0
        if (i, 0) in memo: return memo[(i, 0)]

        left_sum = sum(arr[:i+1])
        right_sum = sum(arr[i:])
        partition_count = dp(i-1)
        for j in range(i):
            if left_sum == right_sum:
                partition_count = max(partition_count, dp(j) + 1)
        memo[(i, 0)] = partition_count
        return partition_count

    return dp(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
