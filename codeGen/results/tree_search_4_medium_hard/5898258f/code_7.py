def max_xor_sum(N, X, A):
    dp = [[0] * (N+1) for _ in range(N+1)]

    # Initialize base case
    for j in range(N+1):
        dp[0][j] = 0

    for i in range(1, N+1):
        for j in range(1, N-i+2):
            if j == i-1:
                dp[i][j] = (A[j]-X) ^ A[j+1]
            else:
                dp[i][j] = max((dp[i-1][k-1] + (A[k]-X) ^ A[k+1]) for k in range(1, i))

    return max(dp[N])

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(N, X, A))
