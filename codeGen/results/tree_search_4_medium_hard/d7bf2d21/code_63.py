def findLongestSubsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    seen = [False] * n
    dp = {i: 1 for i in range(n)}

    for i in range(1, n):
        if not seen[i]:
            seen[i] = True
            for j in range(i):
                if arr[j] < arr[i] and not seen[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        else:
            for j in range(i):
                if arr[j] < arr[i] and not seen[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

    return max(dp.values())

print(findLongestSubsequences())
