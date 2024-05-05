def max_score(arr, k, z):
    memo = {(1, 0): arr[0]}

    for i in range(2, len(arr) + 1):
        memo[(i, 0)] = arr[i - 1]

    for j in range(1, min(k + 1, len(arr))):
        memo[(j, 0)] = max(memo[(j - 1, 0)], arr[j - 1])

    for i in range(2, len(arr) + 1):
        for j in range(min(i, k), 0, -1):
            if j <= z:
                memo[(i, j)] = max(memo[(i - 1, j - 1)], arr[i - 1] + memo[(i - 2, j)])
            else:
                memo[(i, j)] = max(memo[(i - 1, j - 1)], arr[i - 1])

    return memo[(len(arr), k)]
