def max_partitions(arr):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n, -1, -1):
        sum_left = sum(arr[:i])
        sum_right = sum(arr[i:])
        if sum_left == sum_right:
            dp[i][i] = True
        else:
            j = n - 1
            while j >= i:
                if dp[j][j]:
                    dp[i][j] = True
                    break
                j -= 1

    max_partitions = 0
    for i in range(n + 1):
        for j in range(i, -1, -1):
            if dp[j][i]:
                max_partitions = max(max_partitions, i - j)

    return max_partitions

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
