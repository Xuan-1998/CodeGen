from collections import defaultdict

def partition_sum(arr):
    n = len(arr)
    dp = defaultdict(int)

    for i in range(n):
        if i == 0:
            dp[i] = 1
        else:
            left_sum = sum(arr[:i])
            right_sum = sum(arr[i:])
            if left_sum == right_sum:
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-1], 1 + (dp.get(i-1, 0) or 0))

    return dp[n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_sum(arr))
