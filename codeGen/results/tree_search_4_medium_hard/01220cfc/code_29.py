def canJump(arr):
    n = len(arr)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for j in range(i):
            if arr[j] >= i - j and dp[j]:
                dp[i] = True
                break

    return dp[-1]

# Test the function with an array of integers
arr = list(map(int, input().split()))
print(canJump(arr))
