def max_xor_sum(A, X):
    N = len(A)
    dp = [-10**9] * (N + 1)
    dp[0] = 0

    for i in range(1, N):
        dp[i] = max(dp[i-1], dp[i-1] + (A[i]-X) ^ A[i+1])

    return dp[-1]

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
