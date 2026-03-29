def expected_carries(T):
    dp = [0] * (N + 1)
    for _ in range(T):
        N = int(input())
        A, B = map(int, input().split())
        for i in range(2, N + 1):
            dp[i] = sum(dp[j] for j in range(i)) + expected_carries(max(A % 10**i, B % 10**i) - min(A % 10**i, B % 10**i), max(9 * (i - 1), 0), i-1)
        print(dp[N])

def expected_carries(A, B, N):
    if N == 1:
        return max(A, B) // 10
    else:
        return dp[N]

T = int(input())
expected_carries(T)
