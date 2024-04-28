def partition_count(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        cumulative_sum = 0
        j = i
        while j >= 0 and cumulative_sum == 0:
            cumulative_sum += arr[j]
            j -= 1
        dp[i] = max(dp[i], 1 + (dp[j + 1] if j >= 0 else 1))

    return dp[0]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_count(arr))
