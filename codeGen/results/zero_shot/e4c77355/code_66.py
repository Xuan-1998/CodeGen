def longest_increasing_subsequence():
    n = int(input())  # Read the array size from stdin
    arr = list(map(int, input().split()))  # Read the unsorted array from stdin
    dp = [1] * n  # Initialize dynamic programming table with ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(longest_increasing_subsequence())
