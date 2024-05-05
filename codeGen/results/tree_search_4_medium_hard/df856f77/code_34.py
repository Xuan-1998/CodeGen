from collections import deque

def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    queue = deque([(0, 0)])

    while queue:
        i, prev = queue.popleft()
        if i > 0 and arr[i-1] <= arr[i]:
            continue
        for j in range(i+1, n):
            if arr[j-1] <= arr[j]:
                dp[i] = min(dp[i], dp[j-1] + (j - i))
                queue.append((i, j))
                break

    return dp[-1]

N = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
