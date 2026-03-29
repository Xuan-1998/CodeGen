import sys

def max_xor_sum(A, X):
    N = len(A)
    dp = [0]*(N+1)

    for i in range(1, N+1):
        if i == 1:
            dp[i] = A[0]
        else:
            dp[i] = max(dp[i-1], dp[i-2]-X) if i > 1 else 0
            for j in range(i):
                dp[i] = max(dp[i], dp[j] XOR A[i])

    return dp[N-1]

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
