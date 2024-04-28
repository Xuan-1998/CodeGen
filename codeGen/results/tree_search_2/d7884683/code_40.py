from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    dp = defaultdict(int)

    for i in range(n):
        total_sum = sum(arr[:i+1])
        if total_sum not in dp:
            dp[total_sum] = 0
        if total_sum == 0:
            dp[total_sum] = 1
        else:
            for prev_sum, count in list(dp.items()):
                if total_sum - prev_sum > 0 and sum(arr[i+1:]) == total_sum - prev_sum:
                    dp[total_sum] = max(count + 1, dp.get(total_sum, 0))
    return dp[max(dp)]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))

