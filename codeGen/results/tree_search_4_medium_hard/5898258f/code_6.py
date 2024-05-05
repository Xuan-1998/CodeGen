def max_xor_sum(A, X):
    N = len(A)
    dp = [0] * (N + 1)

    for i in range(2, N + 1):
        dp[i] = max(dp[i-1], sum((A[j-1] ^ A[j]) for j in range(i)))

    return max(dp[N//2:] + [dp[N-1] - X] if N % 2 == 0 else dp[N:])

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
