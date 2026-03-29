from collections import deque

def can_jump(arr):
    n = len(arr)
    dp = [False] * n
    dp[0] = True  # We can always start from the beginning
    for i in range(1, n):
        for j in range(i):
            if arr[j] >= i and (i == j + 1 or dp[j]):
                dp[i] = True
    return dp[-1]

arr = list(map(int, input().split()))
print(can_jump(arr))
