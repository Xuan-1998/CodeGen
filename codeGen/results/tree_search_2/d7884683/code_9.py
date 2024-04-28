def max_partitions(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        if not dp[i - 1]:
            continue
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            dp[i] = True

    return sum(dp) - 1  # subtract the initial empty array

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
