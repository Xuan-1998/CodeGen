def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if sum(arr[:j]) == sum(arr[j:i]):
                dp[i] = max(dp[i], dp[j])

    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
