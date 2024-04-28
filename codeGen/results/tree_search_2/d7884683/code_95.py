from collections import defaultdict

def partition_count():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read size of array
        arr = list(map(int, input().split()))  # Read array elements
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        dp = defaultdict(int)
        max_partitions = 0

        for i in range(1, n):
            for k in range(i):
                if prefix_sum[k] == prefix_sum[i] - prefix_sum[k]:
                    dp[i] = max(dp.get(k, 0), dp.get(i - 1, 0)) + 1
                    max_partitions = max(max_partitions, dp[i])

        print(max_partitions)

partition_count()
