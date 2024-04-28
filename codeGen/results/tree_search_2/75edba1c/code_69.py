def solve(N, K, Arr):
    dp = [0] * N
    for i in range(1, N):
        if max(Arr[:i+1]) > K:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    return sum(dp) - dp[0]

# Example usage:
N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(solve(N, K, Arr))
