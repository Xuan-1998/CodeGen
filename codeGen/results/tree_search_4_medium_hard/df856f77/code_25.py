===BEGIN CODE===
def min_operations(arr):
    n = len(arr)
    dp = [0] * n
    prev = [-1] * n

    for i in range(1, n):
        max_prev = -1
        for j in range(i):
            if arr[j] <= arr[i]:
                max_prev = j
                break

        if max_prev != -1:
            dp[i] = min(dp[max_prev] + 1, dp[i-1])
        else:
            dp[i] = dp[i-1]

    return dp[-1]

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
