===BEGIN CODE===
def solve():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(2, N + 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + A[i-1] ^ X)
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] - A[i-1] ^ X)
        print(max(dp[-1]))

solve()
===END CODE===
