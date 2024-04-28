from collections import defaultdict

def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        dp = defaultdict(int)
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                if sum(arr[:i]) == sum(arr[i:]):
                    dp[(i, j)] = max(dp.get((i, j), 0) + 1, 1)
        
        print(max(sum(1 for k, v in dp.items() if all(i <= i2 and j >= j2 for (i2, j2) in v)), 0))

max_partitions()
