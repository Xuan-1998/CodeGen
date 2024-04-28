from collections import defaultdict

def partition_times(n, arr):
    dp = [0] * (n + 1)
    left_sum = sum(arr[:n//2])
    right_sum = sum(arr[n//2:])
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            left_sum += arr[i - 1]
            right_sum -= arr[i - 1]
        else:
            dp[i] = dp[i - 1]
        for j in range(i):
            if sum(arr[:j]) == sum(arr[j:]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_times(n, arr))
