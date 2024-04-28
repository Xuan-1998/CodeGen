def count_subarrays(N, K, Arr):
    dp = {}
    count = 0

    for i in range(N):
        max_val = max(dp.get((i-1, Arr[i-1]), (0, 0))[1], Arr[i])
        if max_val > K:
            count += 1
        dp[(i, max_val)] = None

    return count
