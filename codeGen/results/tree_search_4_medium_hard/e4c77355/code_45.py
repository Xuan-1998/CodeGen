def longest_increasing_subsequence(arr):
    n = len(arr)
    DP = [[1] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                DP[i][j] = max(DP[i][j], DP[j][k] + 1)  # k is the previous element

    return max(max(row) for row in DP)
