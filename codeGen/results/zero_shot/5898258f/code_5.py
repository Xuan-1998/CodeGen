def max_xor_sum(A, X):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(1, N):
        dp[i] = dp[i-1] ^ A[i]
    max_sum = 0
    for i in range(N):
        if dp[i] > X:
            break
        max_sum += dp[i]
    return max_sum

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
