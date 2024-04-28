def count_subarrays(K, Arr):
    N = len(Arr)
    memo = {}
    res = 0

    for i in range(N):
        max_val = max(memo.get((i-1, max_val), (0,)))[1] if i > 0 else 0
        if Arr[i] > K:
            res += 1
        memo[(i, max_val)] = res

    return res
