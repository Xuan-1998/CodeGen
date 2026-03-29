def can_partition(arr):
    N, K, M = len(arr), 0, 0
    for x in arr:
        if x > M:
            M = x
        K = max(K, x)
    memo = {(i, j): False for i in range(N+1) for j in range(M+1)}
    for i in range(1, N+1):
        for j in range(1, min(i, M)+1):
            if (all(x-M <= y and y-x <= M for x, y in zip(arr[:i], arr[i-1::-1]))) or \
               any((dp[i-p][k] for p in range(j) for k in range(K+1)) and dp[i-p][k]):
                memo[(i, j)] = True
    return memo.get((N, M), False)
