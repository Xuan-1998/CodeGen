def max_partitions(arr):
    n = len(arr)
    dp = {0: 1}  # base case: single-element array can always be partitioned once
    for i in range(n-1, -1, -1):
        left_sum = sum(arr[:i+1])
        if left_sum in dp:
            dp[i] = dp.get(i, 0) + dp[left_sum]
        else:
            dp[i] = 0
    return max(dp.values())

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
