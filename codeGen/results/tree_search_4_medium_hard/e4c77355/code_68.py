def longest_increasing_subsequence():
    n = int(input())
    arr = [int(x) for x in input().split()]
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_length = 0
        for j in range(i):
            if arr[i - 1] > arr[j]:
                max_length = max(max_length, dp[j] + 1)
        dp[i] = max_length

    return max(dp)

print(longest_increasing_subsequence())
