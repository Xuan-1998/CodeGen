def canJump(arr):
    n = len(arr)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for j in range(min(i, arr[i-1]), 0, -1):
            if dp[j]:
                dp[i] = True
                break

    return dp[-1]

# Example usage:
arr = list(map(int, input().split()))
print(canJump(arr))
