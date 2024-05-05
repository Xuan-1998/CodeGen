def longest_increasing_subsequence(arr):
    n = len(arr)
    DP = [1] * n  # Initialize with ones (subsequences of length 1)

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                DP[i] = max(DP[i], DP[j] + 1)

    return max(DP)
