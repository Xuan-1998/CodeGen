def max_xor_sum(A, X):
    N = len(A)
    dp = {0: 0}

    for i in range(1, N+1):
        if i-1 not in dp:
            dp[i] = dp[i-1]
        else:
            dp[i] = max(dp.get(i-1, 0), A[i-1] ^ (dp[i-1]-X))

    return max(dp.values())

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
