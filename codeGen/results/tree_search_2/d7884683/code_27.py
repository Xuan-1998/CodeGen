def max_partitions(arr):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        j = 1
        while j <= i:
            if left_sum == right_sum:
                dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 else 0)
            j += 1

    return max(dp[-1])

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
