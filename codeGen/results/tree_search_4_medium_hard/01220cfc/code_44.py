def canReach(arr):
    dp = [False] * len(arr)
    dp[0] = True
    for i in range(1, len(arr)):
        for j in range(i):
            if j + 1 <= i and j <= min(i - arr[j], j) and dp[j]:
                dp[i] = True
                break
    return dp[-1]

arr = list(map(int, input().split()))
print(canReach(arr))
